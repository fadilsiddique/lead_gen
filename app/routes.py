from flask import Blueprint, request, jsonify
from app.google_places import get_leads

main = Blueprint("main", __name__)

@main.route("/leads", methods=["GET"])
def leads():
    keyword = request.args.get("q")
    location = request.args.get("location", "25.276987,55.296249")  # Default: Dubai

    if not keyword:
        return jsonify({"error": "Missing 'q'"}), 400

    leads = get_leads(keyword, location)
    return jsonify(leads)
