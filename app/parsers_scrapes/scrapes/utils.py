"""Methods to be used by adjacent modules"""
from typing import AnyStr

from slack import WebClient
from slack.errors import SlackApiError


def send_response(slack_client: WebClient,
                  channel: AnyStr = "ideas",
                  response: AnyStr = None) -> None:
    """
    This method takes a string as input
    and sends the items to a specified channel
    :param slack_client: WebClient
    :param channel: Channel to send the data to a specified channel
    :param response: List of items
    :return: None
    """
    try:
        slack_client.chat_postMessage(channel=channel, text=response)
    except SlackApiError:
        raise ConnectionError("Invalid slack client URL, check config")
