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

import random
import requests

from string import ascii_uppercase

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

def generate_stocks(number):
    """Generate random list of stocks"""
    stocks = ['AXA']
    for i in range(number-1):
        stocks.append("".join(random.choices(ascii_uppercase, k=3)))
    
    return stocks


class FillServer:
    """Prepare trade fills"""
    
    def __init__(self):
        pass

    def __str__(self):
        return f"{type(self).__name__}"

    def __repr__(self):
        return f"{type(self).__name__}()"

    def prepare_payload(self):
        return {
            "stock_ticker": random.choice(STOCKS),
            "price": float(f"{random.uniform(1, 40):.2f}"),
            "quantity": random.randint(1, 100)
        }

    def send_payload(self) -> None:
        url = "http://controller:8000/data/fill"
        payload = self.prepare_payload()
        response = requests.post(
            url=url,
            json=payload
        )

STOCKS = generate_stocks(10)
print(f"Available stocks: {STOCKS}")

app = FastAPI()

@app.on_event('startup')
@repeat_every(seconds=10)
async def send_data():
    fill_server = FillServer()
    fill_server.send_payload()