import feedparser

DEN_OF_GEEK_RSS_FEED = "http://denofgeek.com/us/feeds/all"


def get_top_10_dog(slack_client) -> None:
    """
    This method fetches top 10 news articles and sends them as links
    To the specified channel
    :param slack_client:
    :return: None
    """
    parsed_data = feedparser.parse(DEN_OF_GEEK_RSS_FEED)
    slack_block = [{"type":
                        "section",
                    "text":
                        {"type": "mrkdwn",
                         "text": ""
                         }
                    }]

    slack_block[0]["text"]["text"] = "*Den of Geek*"

    slack_client.chat_postMessage(channel="#ideas", blocks=slack_block)
    for news_item in parsed_data["entries"]:
        slack_text = "<{}|{}>".format(news_item["link"], news_item["title"])
        slack_block[0]["text"]["text"] = slack_text
        slack_client.chat_postMessage(channel="#ideas", blocks=slack_block)
