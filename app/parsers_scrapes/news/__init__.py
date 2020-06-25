from .den_of_geek import get_top_10_dog

RSS_FEEDS = {"DOG": get_top_10_dog}


def get_news(slack_client, source):
    """
    Based on source which can be any of the values from RSS_FEEDS
    This method fetches news from a specific RSS Feed and returns to slack
    :param slack_client:
    :param source:
    :return:
    """
    RSS_FEEDS.get(source[0])(slack_client)
