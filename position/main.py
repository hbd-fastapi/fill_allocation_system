"""
    Position server

    - receive report from controller at 10 second intervals
    - prints out new positions/values

"""

from typing import Dict

from fastapi import FastAPI


class PositionServer:
    """Process the data from controller"""
    
    RUNS = 0

    def __init__(self, accounts):
        self.accounts = accounts

        PositionServer.RUNS += 1

    def __str__(self):
        return f"{type(self).__name__}"

    def __repr__(self):
        return f"{type(self).__name__}()"

    def process_response(self):
        for account, value in self.accounts.items():
            print(f"{account.capitalize()}: {value}")


app = FastAPI()


@app.post("/positions/")
def positions(payload: Dict):
    position_server = PositionServer(payload)
    position_server.process_response()