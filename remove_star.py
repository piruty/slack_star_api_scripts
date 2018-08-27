# /usr/bin/env python
# coding: utf-8

import os
import sys
import requests

if len(sys.argv) < 2:
    print("Path channel id and timestamp.")
    exit(1)

params = {"channel": sys.argv[1], "timestamp": sys.argv[2]}

url = "https://slack.com/api/stars.remove"
header = {
    "Content-Type": "application/x-www-form-urlencoded; application/json",
    "Authorization": f"Bearer {os.getenv('SLACK_API_TOKEN')}"
}

response = requests.post(url, headers=header, params=params)
data = response.json()
# response json dict sample
#
# Success
# {"ok": true}
#
# Fail
# {"ok": false, "error": "invalid_auth"}

if not data["ok"]:
    print("Fail to remove starred item.")
    exit(1)

print("Remove starred item successfully.")
