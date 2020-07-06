import json
from typing import AnyStr

import pika
from slack import WebClient


def setup_mq(config):
    """
    This method takes a config dict as input and
    initializes a message channel object
    returning a dict of channel, exchange_name and routing_key
    :param config: Dictionary of config values
    :return: Dict of channel, exchange and routing_key
    """
    url = config['CLOUDAMQP_URL']
    try:
        params = pika.URLParameters(url)
    except IndexError:
        raise ValueError("Invalid message queue URL, please fix the config")
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=config["QUEUE_NAME"])
    return channel, connection


def validate_config(config_json: json) -> None:
    """
    This method validates config to find out whether all
    The required values are present or not
    In case any of them are missing,
    stops the execution and raises error
    :param config_json:
    :return:
    """
    missing_keys = []
    required_keys = \
        [
            "CLOUDAMQP_URL",
            "EXCHANGE",
            "QUEUE_NAME",
            "ROUTING_KEY",
            "SECRET_SIGNING_KEY",
            "SLACK_SIGNING_SECRET",
        ]
    for key in required_keys:
        if key not in config_json.keys():
            missing_keys.append(key)

    if len(missing_keys):
        raise ValueError("Please fix the json with "
                         "valid values for the following keys: "
                         "{}".format(', '.join(missing_keys)))


def get_slack_client(signing_key: AnyStr) -> WebClient:
    """
    This method returns the slack client,
    which is used to post messages on channels
    :param signing_key: Secret signing key from config
    :return: Slack WebClient
    """
    return WebClient(signing_key)
