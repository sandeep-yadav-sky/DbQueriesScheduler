import json
import sys
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class SlackNotification:

    def __init__(self):
        self.url = os.getenv("webhookURL")

    def post_to_slack_channel(self,message="",title=""):
        slack_data = {
            "username": "NotificationBot",
            "icon_emoji": ":satellite:",
            "attachments": [
                {
                    "color": "#9733EE",
                    "fields": [
                        {
                            "title": title,
                            "value": message,
                            "short": "false",
                        }
                    ]
                }
            ]
        }
        byte_length = str(sys.getsizeof(slack_data))
        headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
        response = requests.post(self.url, data=json.dumps(slack_data), headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)