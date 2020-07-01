"""Init file for news module"""
from typing import AnyStr
from slack import WebClient

from .den_of_geek import get_top_10_dog
from .screen_rant import get_screen_rant_news

RSS_FEEDS = {
    "DOG": get_top_10_dog,
    "SR": get_screen_rant_news
}


def get_news(slack_client: WebClient, source: AnyStr):
    """
    Based on source which can be any of the values from RSS_FEEDS
    This method fetches news from a specific RSS Feed and returns to slack
    :param slack_client:
    :param source:
    :return:
    """
    RSS_FEEDS.get(source[0])(slack_client)
