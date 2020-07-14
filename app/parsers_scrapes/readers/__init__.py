"""Init file for reader module"""
from typing import AnyStr

import feedparser

from .constants import RSS_FEEDS, \
                       FEEDPARSER_AGENT
from .utils import get_source, \
                   send_empty_response,  \
                   send_heading, \
                   send_response

from ...utils import get_slack_client


def generic_feed_parser(slack_signing_key: AnyStr, source_key: AnyStr):
    """
    This method reads rss feed from a url
    Based on the source_key provided as input
    and posts message on the channel specified
    along with heading
    :param slack_signing_key: Signing key to initialize slack client
    :param source_key: String to find the source where to fetch RSS from
    :return:
    """
    slack_client = get_slack_client(slack_signing_key)
    source = get_source(source_key)
    if not source:
        send_empty_response(slack_client)
    else:
        data_from_rss = feedparser.parse(source['url'],
                                         agent=FEEDPARSER_AGENT)
        heading = source['heading']
        send_heading(slack_client, "#ideas", heading)
        send_response(slack_client, "#ideas", data_from_rss['entries'])
