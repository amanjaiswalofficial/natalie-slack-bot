from bs4 import BeautifulSoup
import urllib

ITEM_URL = "https://www.imdb.com{}"
IMDB_SEARCH_URL = "https://www.imdb.com/find?q={}&ref_=nv_sr_sm"
#
# child = list(res.children)
# child[2]
# child[2].children
#
# child2[3].find_all("script")[1]

def fetch_imdb_results(slack_client, arguments):
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
        slack_client.chat_postMessage(channel="#ideas", text=page_url)
