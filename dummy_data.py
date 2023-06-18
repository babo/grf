#!/usr/bin/env python3

import os
import random
import time

import influxdb_client
import requests

from influxdb_client.client.write_api import SYNCHRONOUS

cities = [("Holmestrand", 59.477110, 10.319426), ("Telki", 47.545134, 18.834282)]


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

    for value in range(4):
        point = (
            influxdb_client.Point("measurement1").tag("tagname1", "tagvalue1").field("field1", value).field("field2", random.gauss(20, 2))
        )
        write_api.write(bucket=bucket, org="primary", record=point)
        time.sleep(15)  # separate points by 15 second

    query_api = write_client.query_api()

    query = """from(bucket: "madar")
        |> range(start: -10m)
        |> filter(fn: (r) => r._measurement == "measurement1")
        |> mean()"""
    tables = query_api.query(query, org="primary")

    for table in tables:
        for record in table.records:
            print(record)


if __name__ == "__main__":
    main()
