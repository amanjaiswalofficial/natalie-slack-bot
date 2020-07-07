from typing import AnyStr, List

from bs4 import BeautifulSoup
import urllib

from slack import WebClient

from app.parsers_scrapes.scrapes.utils import send_response
from app.utils import get_slack_client

ITEM_URL = "https://www.imdb.com{}"
IMDB_SEARCH_URL = "https://www.imdb.com/find?q={}&ref_=nv_sr_sm"


def fetch_imdb_results(slack_signing_key: AnyStr, arguments: List):
    """
    This method searches IMDb and returns the links to post on
    channel #ideas
    :param slack_signing_key:
    :param arguments:
    :return:
    """
    slack_client = get_slack_client(slack_signing_key)

    command = "+".join(arguments)
    search_url = IMDB_SEARCH_URL.format(command)
    response = urllib.request.urlopen(search_url)
    response = response.read().decode("utf-8")
    response = BeautifulSoup(response, "html.parser")

    body = list(response.find_all("table", {"class": "findList"}))
    table = body[0].find_all("tr")
    for row in table:
        url_to_open = row.findAll("a")[-1]
        page_url = ITEM_URL.format(url_to_open.attrs['href'])
        send_response(slack_client=slack_client, response=page_url)
