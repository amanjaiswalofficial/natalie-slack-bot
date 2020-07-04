"""Script to automatically push news to specific channels"""
import json
import sys

from urllib.error import URLError
from slack.errors import SlackApiError
from slack import WebClient

from app.parsers_scrapes.news import *

# channel to post content on
CHANNEL_TO_POST = {
    "DEN_OF_GEEK": "den-of-geek",
    "SCREEN_RANT": "screen-rant"
}

# load secret signing key for slack-bot to post
with open('./config.json') as config_file:
    config_values = json.load(config_file)

slack_client = WebClient(config_values["SECRET_SIGNING_KEY"])
try:
    # each method will post news to a different source
    get_top_10_dog(slack_client, channel=CHANNEL_TO_POST["DEN_OF_GEEK"])
    get_screen_rant_news(slack_client, channel=CHANNEL_TO_POST["SCREEN_RANT"])

    # if all succeeded, will return exit code 0
    sys.exit()
except (URLError, SlackApiError):

    # if anything failed due to any error, will return exit code 127
    sys.exit(127)
