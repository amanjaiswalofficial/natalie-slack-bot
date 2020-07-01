"""Constants for the news module"""
DEN_OF_GEEK_RSS_FEED = "http://denofgeek.com/us/feeds/all"
SCREEN_RANT_RSS_FEED = "https://screenrant.com/feed/"

FEEDPARSER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) ' \
                   'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                   'Chrome/71.0.3578.98 Safari/537.36'
SLACK_BLOCK = [{"type": "section",
                "text":
                    {"type": "mrkdwn",
                     "text": ""
                     }
                }]