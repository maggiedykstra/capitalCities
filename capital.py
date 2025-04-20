from flask import Flask, jsonify, request
from functools import wraps
from datetime import datetime
import pytz

app = Flask(__name__)

# API Token for authentication
API_TOKEN = "supersecrettoken123"

# Hardcoded information for capital cities (city, timezone)
CAPITAL_CITIES = {
    "London": {"timezone": "Europe/London"},
    "New York": {"timezone": "America/New_York"},
    "Tokyo": {"timezone": "Asia/Tokyo"},
    "Sydney": {"timezone": "Australia/Sydney"},
    "Paris": {"timezone": "Europe/Paris"},
    "Berlin": {"timezone": "Europe/Berlin"},
    "Moscow": {"timezone": "Europe/Moscow"},
    "Delhi": {"timezone": "Asia/Kolkata"},
    "Beijing": {"timezone": "Asia/Shanghai"},
    "Cairo": {"timezone": "Africa/Cairo"},
    "Ottawa": {"timezone": "America/Toronto"},
    "Brasilia": {"timezone": "America/Sao_Paulo"},
    "Buenos Aires": {"timezone": "America/Argentina/Buenos_Aires"},
    "Cape Town": {"timezone": "Africa/Johannesburg"},
    "Seoul": {"timezone": "Asia/Seoul"},
    "Singapore": {"timezone": "Asia/Singapore"},
    "Mexico City": {"timezone": "America/Mexico_City"},
    "Los Angeles": {"timezone": "America/Los_Angeles"}
}

# Token protection decorator
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    return decorator

@app.route('/')
def index():
    return "This is the Capital Time API. Use /api/time?city=CapitalName to get the time for a capital city."

@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Missing 'city' query parameter"}), 400

    city = city.capitalize()  # Capitalize city name for case-insensitive matching
    city_info = CAPITAL_CITIES.get(city)

    if not city_info:
        return jsonify({"error": f"City '{city}' not found in database"}), 404

    timezone_str = city_info["timezone"]

    try:
        tz = pytz.timezone(timezone_str)
        now = datetime.now(tz)
        utc_offset = now.strftime('%z')
        return jsonify({
            "city": city,
            "local_time": now.strftime('%Y-%m-%d %H:%M:%S')
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)