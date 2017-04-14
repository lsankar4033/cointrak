"""Cointrak. A toolset for keeping track of cryptocurrency. TODO moar tools (see README)

Usage:
  ct.py [-n NUM_RESULTS]

Options:
  -h --help                                 Show this screen.
  --version                                 Show version.
  -n NUM_RESULTS --num-results=NUM_RESULTS  Number of cryptocurrencies to check  [default: 10].
"""
import utils
from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(__doc__, version="cointrak 0.1")
    num_results = arguments["--num-results"]

    json_resp = utils.get_ticker_json(num_results)

    utils.print_response_json(json_resp,
                              ["name",
                               "price_usd",
                               "percent_change_1h",
                               "percent_change_24h",
                               "percent_change_7d"])
