from flask import Blueprint, jsonify, request

weather_blueprint = Blueprint("weather", __name__)

@weather_blueprint.route("/weather", methods=["GET"])
def get_weather() -> dict:
    city = request.args.get("city", "Unknown")

    response = {
        "city": city,
        "temperature": 25,
        "conditions": "sunny"
    }

    return jsonify(response), 200
