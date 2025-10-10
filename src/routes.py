from flask import Blueprint, jsonify, request
import requests
from config import Settings
from src.services.cache import get_cache, set_cache

settings = Settings()

weather_blueprint = Blueprint("weather", __name__)

@weather_blueprint.route("/weather", methods=["GET"])
def get_weather() -> dict:
    city = request.args.get("city", "Unknown")

    cached_data = get_cache(city.lower())
    if cached_data:
        cached_data["cached"] = True
        cached_data["success"] = True
        return cached_data, 200

    try:
        url = (
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/"
            f"timeline/{city}?unitGroup=metric&key={settings.API_KEY}&contentType=json"
        )
        response = requests.get(url)

        data = response.json()
        weather = {
            "city": city,
            "temperature": data["currentConditions"]["temp"],
            "conditions": data["currentConditions"]["conditions"],
            "source": "Visual Crossing"
        }

        set_cache(city.lower(), weather)

        return jsonify(weather), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
