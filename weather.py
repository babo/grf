#!/usr/bin/env python3

import os
import random
import time

import influxdb_client
import requests

from influxdb_client.client.write_api import SYNCHRONOUS

cities = [("Holmestrand", 59.477110, 10.319426), ("Telki", 47.545134, 18.834282), ("Yokohama", 35.455445, 139.638240)]


def get_weather(latitude, longitude):
    params = {"current_weather": True, "latitude": latitude, "longitude": longitude}
    resp = requests.get("https://api.open-meteo.com/v1/forecast", params)
    assert resp.ok
    return resp.json()


def main():
    bucket = "madar"
    org = "primary"
    token = os.environ.get("INFLUXDB_TOKEN")
    url = "http://localhost:28086"

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    write_api = write_client.write_api(write_options=SYNCHRONOUS)

    for city, lat, lng in cities:
        point = influxdb_client.Point("weather").tag("city", city)
        weather = get_weather(lat, lng)
        for k, v in weather["current_weather"].items():
            if k != "time":
                point.field(k, v)
        write_api.write(bucket=bucket, org=org, record=point)
        print(city, "=>", " ".join([f"{k}: {v}" for k, v in weather["current_weather"].items()]))


if __name__ == "__main__":
    main()
