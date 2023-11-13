import json
from app import app
from flask import jsonify
from urllib.request import urlopen

@app.route("/weather")
def hw01_localweather():
    return app.send_static_file("hw01_localweather.html")

@app.route("/api/weather")
def api_weather():
    res = urlopen("https://api.waqi.info/feed/here/?token=7af3dd2f0ebfd5bda114fbbc3fb501edebf05c33")
    dict_data = json.load(res)["data"]
    return jsonify({
        "city": dict_data["city"]["name"],
        "data": {
            "AQI": dict_data["aqi"],
            "PM10": dict_data["iaqi"]["pm10"]["v"],
            "PM2.5": dict_data["iaqi"]["pm25"]["v"],
            "Temperature": dict_data["iaqi"]["t"]["v"],
            "Time": dict_data["time"]["iso"]
        }
    })
