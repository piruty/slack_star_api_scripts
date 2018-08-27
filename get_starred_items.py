# /usr/bin/env python
# coding: utf-8

import os
import requests

url = "https://slack.com/api/stars.list"
header = {"Content-Type": "application/x-www-form-urlencoded"}
params = {"token": os.getenv("SLACK_API_TOKEN")}

response = requests.get(url, headers=header, params=params)
data = response.json()
# response json dict sample
#
# Success
# {
#     "ok": true,
#     "items": [
#         {
#             "type": "message",
#             "channel": "channel_id",
#             "message": {
#                 "type": "message",
#                 "user": "user_id",
#                 "text": "text message",
#                 "client_msg_id": "client-message-id",
#                 "ts": "1535345930.000100",
#                 "permalink": "link/to/slack/message",
#                 "is_starred": true
#             },
#             "date_create": 1535345934
#         }
#     ],
#     "response_metadata": {
#         "next_cursor": ""
#     }
# }
#
# Fail
# {"ok": false, "error": "invalid_auth"}

if not data["ok"]:
    print("Could not get starred items.")
    exit(1)

messages = []
for item in data["items"]:
    messages.append(item["message"])


def make_result(messages: list):
    """
    Make result string from passed message list

    :param messages: message list (look above to check details)
    :return: formatted message
    """
    if not messages:
        return "There were no starred items."
    text = ""
    for m in messages:
        if len(text) > 0:
            text += "\n"
        text += f"□ {m['text']}\n   {m['permalink']}\n"
    return "Stared Items\n\n" + text


print(make_result(messages))
