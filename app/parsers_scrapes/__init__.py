from app.parsers_scrapes.scrapes.\
    imdb_fetch_search_results import fetch_imdb_results
from app.parsers_scrapes.news import get_news

run_command = {
    "find": fetch_imdb_results,
    "read": get_news
}
