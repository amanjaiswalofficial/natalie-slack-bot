from app.parsers_scrapes.scrapes.\
    imdb_fetch_search_results import fetch_imdb_results
from app.parsers_scrapes.readers import generic_feed_parser

run_command = {
    "find": fetch_imdb_results,
    "read": generic_feed_parser
}
