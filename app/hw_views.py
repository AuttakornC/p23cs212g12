# นายอรรถกร คำสร้อย เอิร์ธ
# 650510691
# Sec001

import json
from app import app
from flask import jsonify, render_template
from urllib.request import urlopen

from datetime import datetime

@app.route("/weather")
def hw01_localweather():
    return app.send_static_file("hw01_localweather.html")

@app.route("/api/weather")
def api_weather():
    res = urlopen("https://api.waqi.info/feed/ChiangMai/?token=7af3dd2f0ebfd5bda114fbbc3fb501edebf05c33")
    dict_data = json.load(res)["data"]
    return jsonify({
        "AQI": dict_data["aqi"],
        "PM10": dict_data["iaqi"]["pm10"]["v"],
        "PM2.5": dict_data["iaqi"]["pm25"]["v"],
        "Temperature": dict_data["iaqi"]["t"]["v"],
        "Time": dict_data["time"]["iso"]
    })

@app.route("/hw03/pm25/")
def hw03_pm25():
    res = urlopen("https://api.waqi.info/feed/ChiangMai/?token=7af3dd2f0ebfd5bda114fbbc3fb501edebf05c33")
    dict_data = json.load(res)["data"]["forecast"]["daily"]["pm25"]
    first_date = list(map(lambda x: int(x) ,dict_data[0]["day"].split("-")))
    day = datetime(first_date[0], first_date[1], first_date[2]).weekday()
    dict_data = (["-" for i in range((day+1)%7)]) + dict_data
    week_split = []
    week = []
    before = "-"
    for i in dict_data:
        if i != "-":
            if before == "-":
                i["status"] = "-"
            elif i["avg"] == before:
                i["status"] = "eq"
            elif i["avg"] > before:
                i["status"] = "gt"
            else:
                i["status"] = "lt"
            before = i["avg"]

            if i["avg"] <= 50:
                i["color"] = "good"
            elif i["avg"] <= 100:
                i["color"] = "moderate"
            elif i["avg"] <= 150:
                i["color"] = "unhealthy-sensitive"
            elif i["avg"] <= 200:
                i["color"] = "unhealthy"
            elif i["avg"] <= 300:
                i["color"] = "very-unhealthy"
            else:
                i["color"] = "hazardous"
        week.append(i)
        if len(week)==7:
            week_split.append(week[:])
            del week[:]
    if len(week)!=7:
        week = week+(["-"]*(7-len(week)))
        week_split.append(week[:])
    return render_template("lab03/hw03_pm25.html", datas=week_split, first_day=day)
