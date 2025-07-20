# 🧲 Google Business Lead Scraper (Flask + Places API)

This Flask app helps you **generate business leads** using the [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview).

Pass in a **business type** and **location name**, and you'll get enriched JSON output including:
- ✅ Business name
- ✅ Address
- ✅ Phone number
- ✅ Website (if available)
- ✅ Star rating

Built with **caching**, **structured code**, and **n8n compatibility** for full automation into Google Sheets or CRMs.

---

## 📦 Features

- 🔎 Uses Google Places API `textsearch` and `details`
- 📍 Converts location names to coordinates using Geocoding API
- 📞 Returns phone numbers and websites
- 🧠 Caches results for 1 hour (avoid repeated API cost)
- 📊 Designed for lead generation via tools like [n8n](https://n8n.io/)

---

## 🛠️ Tech Stack

- Python 3
- Flask
- Google Maps Platform APIs:
  - Places API
  - Geocoding API
- dotenv
- n8n-compatible JSON API

---

## 🚀 How It Works

### Example:


Returns:
json ```
[
  {
    "name": "ABC Business Consulting",
    "address": "Oud Metha, Dubai, UAE",
    "phone": "+971 50 123 4567",
    "website": "https://abcconsulting.ae",
    "rating": 4.3
  },
  ...
]```
🧰 Setup Instructions
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/your-username/lead-scraper.git
cd lead-scraper
2. Install Dependencies
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Add Your Google API Key
Create a .env file in the root directory:

ini
Copy
Edit
GOOGLE_API_KEY=your-real-api-key-here
Required APIs:

✅ Places API

✅ Geocoding API

Enable both via Google Cloud Console.

4. Run the Server
bash
Copy
Edit
python run.py
The app will run on:

arduino
Copy
Edit
http://localhost:5000
📡 Available API Routes
GET /leads
Query Param	Description	Required
q	Business category / search keyword	✅ Yes
location	Area or region (e.g. "Dubai Marina")	✅ Yes


## ⚠️ API Limitations
Google Places textsearch doesn’t return phone/website by default

We use Places Details API to enrich each result — this means 2 requests per lead

You're allowed:

✅ 150,000 textsearch requests/month free

✅ 11,000 details requests/month free

More than enough for lead gen
