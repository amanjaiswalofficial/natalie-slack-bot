"""Constants for the news module"""
RSS_FEEDS = {
    "dog": {
        "heading": "Den Of Geek",
        "url": "http://denofgeek.com/us/feeds/all"
    },
    "den_of_geek": {
        "heading": "Den Of Geek",
        "url": "http://denofgeek.com/us/feeds/all"
    },
    "sr": {
        "heading": "Screen Rant",
        "url": "https://screenrant.com/feed/"
    },
    "screen_rant": {
        "heading": "Screen Rant",
        "url": "https://screenrant.com/feed/"
    }
}

FEEDPARSER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) ' \
                   'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                   'Chrome/71.0.3578.98 Safari/537.36'
SLACK_BLOCK = [{"type": "section",
                "text":
                    {"type": "mrkdwn",
                     "text": ""
                     }
                }]

ERROR_404_MESSAGE = "Invalid choice for RSS Feed, " \
                    "please try 'help read' to get " \
                    "all valid options for RSS feeds"
