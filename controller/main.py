import requests

from typing import Dict

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every


class ControllerServer:
    """
    Process trade fills
    Process account splits
    """
    FILLS = []
    position = {"account1": 0, "account2": 0, "account3": 0, "account4": 0}


    def __init__(self, accounts=None):
        self.accounts = accounts

    def __str__(self):
        return f"{type(self).__name__}"

    def __repr__(self):
        return f"{type(self).__name__}()"

    def add_fills(cls, payload):
        cls.FILLS.append(payload)

    def new_position(self):
        """Calculate new positions for accounts"""
        # TODO: Refactor this function

        accounts = self.accounts
        fills = ControllerServer.FILLS[-1]

        quantity = fills['quantity']
        stocks = []
        for key, value in accounts.items():
            stocks.append(round(value/100 * quantity))

        summary = sum([fill['quantity'] for fill in self.FILLS])
        ideal_position = {account: summary*value/100 for account, value in self.accounts.items()}
        current_fill = self.FILLS[-1]['quantity']

        for stock in range(current_fill):
            for key, value in self.position.items():

                if value < ideal_position[key]:
                    self.position[key] += 1
                    break
        
        return self.position

    def send_payload(self) -> None:
        """Send payload to position server"""
        url = "http://position:8000/positions"
        payload = self.new_position()
        response = requests.post(
            url=url,
            json=payload
        )
    
    def process_aum_response(self, payload):
        """Prints percentages during next split"""
        print(f"Next split:")
        for account, percentage in payload.items():
            print(f"{account.capitalize()}: {percentage}")


app = FastAPI()
controller_server = ControllerServer()

@app.post("/data/fill")
async def get_fills(payload: Dict):
    controller_server.add_fills(payload)
    print(f"Buy {payload['quantity']} {payload['stock_ticker']} for {payload['price']}")

@app.post("/data/aum")
async def get_aum(payload: Dict):
    controller_server.accounts = payload
    controller_server.process_aum_response(payload)

@app.on_event('startup')
@repeat_every(seconds=10)
async def send_data():
    controller_server.send_payload()