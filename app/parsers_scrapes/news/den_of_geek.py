"""File containing parsing method for den of geek"""
from typing import AnyStr

import feedparser

from app.parsers_scrapes.news.constants import DEN_OF_GEEK_RSS_FEED
from app.parsers_scrapes.news.utils import send_heading, \
                                           send_response
from app.utils import get_slack_client


def get_top_10_dog(slack_signing_key: AnyStr,
                   channel: AnyStr = "#ideas") -> None:
    """
    This method fetches top 10 news articles and sends them as links
    To the specified channel
    :param slack_signing_key: Signing key from config
    :param channel: Channel to post content on
    :return: None
    """
    slack_client = get_slack_client(slack_signing_key)
    parsed_data = feedparser.parse(DEN_OF_GEEK_RSS_FEED)
    if len(parsed_data):
        send_heading(slack_client, channel, "Den of Geek")
        send_response(slack_client, channel, parsed_data["entries"])
