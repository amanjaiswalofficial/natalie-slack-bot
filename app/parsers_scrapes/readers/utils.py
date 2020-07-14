"""Utility methods for sending messages to Slack"""
from typing import AnyStr, List, Dict
from slack import WebClient
from slack.errors import SlackApiError

from app.parsers_scrapes.readers.constants import RSS_FEEDS, \
    SLACK_BLOCK, ERROR_404_MESSAGE


def get_source(source_string: AnyStr) -> Dict:
    """
    This method finds the rss feed object based on source string
    :param source_string: String acting as key to find RSS feed source
    :return:
    """
    source = "_".join([word.lower() for word in source_string])
    return RSS_FEEDS.get(source)


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


def send_empty_response(slack_client: WebClient) -> None:
    """
    This method sends not found error message to the slack chat
    :param slack_client: SlackClient to post message
    :return: None
    """
    try:
        slack_client.chat_postMessage(channel="#ideas",
                                      text=ERROR_404_MESSAGE)
    except SlackApiError:
        raise ConnectionError("Invalid slack client URL, check config")
