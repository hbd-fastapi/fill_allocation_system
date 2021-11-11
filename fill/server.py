"""
    Fill Server

    - sends trade fills at random intervals
    - uses only 10 stocks that are available
    - payload for the trade fill:
        {
            "stock_ticker": <random stock>,
            "price": <random positive price>,
            "quantity": <random quantity>
        }
"""

import time
import random
import requests

from string import ascii_uppercase


def generate_stocks(count):
    """Generate list of stocks"""
    
    stocks = []
    for i in range(count):
        stocks.append("".join(random.choices(ascii_uppercase, k=3)))
    
    return stocks


def prepare_payload(stocks):
    return {
        "stock_ticker": random.choice(stocks),
        "price": float(f"{random.uniform(1, 40):.2f}"),
        "quantity": random.randint(1, 100)
    }


def connection(url, payload):
    with requests.Session() as s:
        while True:
            
            s.post(
                url=url,
                data=payload
            )
            time.sleep(2)


if __name__ == "__main__":
    stocks = generate_stocks(10)
    payload = prepare_payload(stocks)
    connection("http://controller:8002/fills/", payload)
