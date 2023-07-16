#!/usr/bin/env python3

import os
import random
import time

import influxdb_client

from influxdb_client.client.write_api import SYNCHRONOUS


def main():
    bucket = "madar"
    org = "primary"
    token = os.environ.get("INFLUXDB_TOKEN")
    url = "http://localhost:28086"

    write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
    write_api = write_client.write_api(write_options=SYNCHRONOUS)

    for _ in range(2):
        point = influxdb_client.Point("measurement1") \
            .tag("tagname1", "tagvalue1") \
            .field("field_a", random.gauss(40, 8)) \
            .field("field_b", random.gauss(20, 2))
        write_api.write(bucket=bucket, org="primary", record=point)
        time.sleep(15)  # separate points by 15 second


if __name__ == "__main__":
    main()
