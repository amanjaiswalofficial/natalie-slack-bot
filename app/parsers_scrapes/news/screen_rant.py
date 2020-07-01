"""File containing method for parsing screen rant"""
import feedparser
from slack import WebClient

from app.parsers_scrapes.news.constants import SCREEN_RANT_RSS_FEED, \
                                               FEEDPARSER_AGENT
from app.parsers_scrapes.news.utils import send_heading, \
                                           send_response


def get_screen_rant_news(slack_client: WebClient) -> None:
    """
    This method fetches top 100 news items from ScreenRant RSS Feed
    :param slack_client: WebClient
    :return: None
    """
    parsed_data = feedparser.parse(SCREEN_RANT_RSS_FEED, agent=FEEDPARSER_AGENT)

    if len(parsed_data['entries']):
        send_heading(slack_client, "Screen Rant")
        send_response(slack_client, parsed_data["entries"])
