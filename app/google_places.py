import requests
import os
from dotenv import load_dotenv
from app.cache import Cache

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
cache = Cache()

def geocode_location(location_name):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": location_name,
        "key": API_KEY
    }

    res = requests.get(url, params=params)
    if res.status_code != 200:
        return None

    results = res.json().get("results")
    if not results:
        return None

    location = results[0]["geometry"]["location"]
    return f"{location['lat']},{location['lng']}"

def get_leads(query, location_text, radius=5000, max_results=20):
    query_key = f"{query.lower()}_{location_text.lower()}"
    cached = cache.get(query_key)
    if cached:
        return cached

    # 1. Geocode location
    location_coords = geocode_location(location_text)
    if not location_coords:
        return [{"error": "Could not geocode location"}]

    # 2. Search Places
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    detail_url = "https://maps.googleapis.com/maps/api/place/details/json"

    search_params = {
        "query": query,
        "location": location_coords,
        "radius": radius,
        "key": API_KEY
    }

    res = requests.get(search_url, params=search_params)
    results = res.json().get("results", [])[:max_results]  # Limit to 20

    leads = []
    for place in results:
        place_id = place.get("place_id")
        if not place_id:
            continue

        # 3. Get phone + website
        detail_params = {
            "place_id": place_id,
            "fields": "name,formatted_phone_number,website",
            "key": API_KEY
        }
        detail_res = requests.get(detail_url, params=detail_params)
        details = detail_res.json().get("result", {})

        leads.append({
            "name": place.get("name"),
            "address": place.get("formatted_address"),
            "rating": place.get("rating"),
            "phone": details.get("formatted_phone_number"),
            "website": details.get("website"),
            "maps_link": f"https://www.google.com/maps/place/?q=place_id:{place_id}"
        })

    cache.set(query_key, leads, ttl=3600)
    return leads
