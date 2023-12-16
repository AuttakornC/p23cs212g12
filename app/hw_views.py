# นายอรรถกร คำสร้อย เอิร์ธ
# 650510691
# Sec001

import json
from app import app
from flask import jsonify, render_template
from urllib.request import urlopen

from datetime import datetime, date, timedelta

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

@app.route("/hw04")
def hw04():
    return app.send_static_file("hw04_rwd.html")

MONTH_LIST = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def date_format(str_date:str)->(str, str):
    try:
        str_date = str_date[:10]
        list_date = list(map(int, str_date.split("-")))
        if len(list_date) != 3:
            list_date = list(map(int, str(date.today()).split("-")))
        return f"{list_date[2]} {MONTH_LIST[list_date[1]]} {list_date[0]}", f"{MONTH_LIST[list_date[1]][:3]} {list_date[2]}"
    except:
        str_date = str(date.today())
        list_date = list(map(int, str_date.split("-")))
        return f"{list_date[2]} {MONTH_LIST[list_date[1]]} {list_date[0]}", f"{MONTH_LIST[list_date[1]][:3]} {list_date[2]}"

def get_quality(aqi)->str:
    if isinstance(aqi, str):
        return "unhealthy", "Not Found"
    if aqi <= 50:
        return "good", "Good"
    if aqi <= 100:
        return "moderate", "Moderate"
    if aqi <= 150:
        return "unhealthy-sensitive", "Unhealthy for Sensitive Groups"
    if aqi <= 200:
        return "unhealthy", "Unhealthy"
    if aqi <= 300:
        return "very-unhealthy", "Very Unhealthy"
    return "hazardous", "Hazardous"


@app.route("/hw04/aqicard")
def hw04_aqicard():
    DEFAULT_API = {"aqi": "-", "time": {"s": str(date.today())}, "forecast": {"daily":{"pm25": [{"day":str(date.today()+timedelta(i)), "avg": "-"} for i in range(1, 4)]}}}
    infomations = []
    provinces = ["chiang-mai", "bangkok", "phukett", "ubon-ratchathani"]
    for province in provinces:
        link = f"https://api.waqi.info/feed/{province}/?token=7af3dd2f0ebfd5bda114fbbc3fb501edebf05c33"
        res = urlopen(link)
        dict_data = json.load(res).get("data", DEFAULT_API)
        if isinstance(dict_data, str):
            dict_data = DEFAULT_API
        analy_dict = dict()
        analy_dict["aqi"] = dict_data["aqi"]
        analy_dict["city"] = " ".join(list(map(lambda x: x[0].upper()+x[1:], province.split("-"))))
        dd_mm_yyyy, mm_dd = date_format(dict_data["time"]["s"])
        analy_dict["date"] = dd_mm_yyyy
        forecast = []
        today = dict_data["time"]["s"][:10]
        for i in dict_data["forecast"]["daily"]["pm25"]:
            if i["day"] <= today:
                continue
            forecast_dict = dict()
            forecast_dict["aqi"] = i["avg"]
            full, sub = date_format(i["day"])
            forecast_dict["day"] = sub
            forecast_dict["quality-class"], forecast_dict["quality"] = get_quality(i["avg"])
            forecast.append(forecast_dict)
            if len(forecast) == 3:
                break
        analy_dict["forecast"] = forecast
        analy_dict["quality-class"], analy_dict["quality"] = get_quality(dict_data["aqi"])
        infomations.append(analy_dict)
    return render_template("hw04_aqicard.html", info=infomations)