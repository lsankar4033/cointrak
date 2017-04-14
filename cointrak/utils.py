import requests
from tabulate import tabulate

# TODO improve the naming of this function
def print_response_json(json, headers):
    """Print ticker response in tabular form using the specified headers. The headers are also the keys used to
    extract data from the json.
    """
    rows = []
    for elt in json:
        rows.append([elt[header] for header in headers])

    print(tabulate(rows, headers=headers))

# 'limit' is the number of currencies to get
def get_ticker_json(limit):
    query_str = "" if limit is None else "?limit={}".format(limit)
    url = "https://api.coinmarketcap.com/v1/ticker/{}".format(query_str)

    resp = requests.get(url)
    return resp.json()
