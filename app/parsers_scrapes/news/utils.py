"""Utility methods for sending messages to Slack"""
from typing import AnyStr, List
from slack import WebClient
from slack.errors import SlackApiError

from app.parsers_scrapes.news.constants import SLACK_BLOCK


def send_heading(slack_client: WebClient,
                 channel: AnyStr,
                 title: AnyStr) -> None:
    """
    This method sends the heading of the block of messages describing the
    source they were fetched from
    :param slack_client: WebClient
    :param channel: Channel to post the content on
    :param title: String
    :return: None
    """
    SLACK_BLOCK[0]["text"]["text"] = "*{}*".format(title)
    try:
        slack_client.chat_postMessage(channel=channel, blocks=SLACK_BLOCK)
    except SlackApiError:
        raise ConnectionError("Invalid slack client URL, check config")


def send_response(slack_client: WebClient,
                  channel: AnyStr,
                  list_of_items: List) -> None:
    """
    This method takes a list as input
    and sends the items to a specified channel
    :param slack_client: WebClient
    :param channel: Channel to send the data to a specified channel
    :param list_of_items: List of items
    :return: None
    """
    for news_item in list_of_items:
        slack_text = "<{}|{}>".format(news_item["link"], news_item["title"])
        SLACK_BLOCK[0]["text"]["text"] = slack_text
        try:
            slack_client.chat_postMessage(channel=channel, blocks=SLACK_BLOCK)
        except SlackApiError:
            raise ConnectionError("Invalid slack client URL, check config")
