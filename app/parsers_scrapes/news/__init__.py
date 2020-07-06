"""Init file for news module"""
from typing import AnyStr

from .den_of_geek import get_top_10_dog
from .screen_rant import get_screen_rant_news

RSS_FEEDS = {
    "DOG": get_top_10_dog,
    "SR": get_screen_rant_news
}


def get_news(slack_signing_key: AnyStr, source: AnyStr):
    """
    Based on source which can be any of the values from RSS_FEEDS
    This method fetches news from a specific RSS Feed and returns to slack
    :param slack_signing_key: Signing key to make the WebClient for Slack
    :param source:
    :return:
    """
    RSS_FEEDS.get(source[0])(slack_signing_key)
