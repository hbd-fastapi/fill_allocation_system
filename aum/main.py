import random
import requests

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

class AUMServer:
    """
    AUM - Assets Under Management
    Responsible for preparing payload and sending
    """
    
    def __init__(self):
        pass

    def __str__(self):
        return f"{type(self).__name__}"

    def __repr__(self):
        return f"{type(self).__name__}()"

    def split_percentages(self, count):
        """Returns list with percentages depending on the number of accounts"""
        percentages = []
        for i in range(count):
            value = random.randint(0, 100)
            current_sum = sum(percentages)
            
            if current_sum+value<=100 and i<count-1:
                percentages.append(value)
            else:
                percentages.append(100-current_sum)

        return percentages
    
    def prepare_payload(self):
        """Prepares payload to send"""
        count = random.randint(2, 4)
        percentages = self.split_percentages(count)

        payload = {}
        for i in range(count):
            payload[f'account{i+1}'] = percentages[i]

        return payload

    def send_payload(self) -> None:
        """Sends payload to the controller"""
        url = "http://controller:8000/data/aum"
        payload = self.prepare_payload()
        response = requests.post(
            url=url,
            json=payload
        )

app = FastAPI()

@app.on_event('startup')
@repeat_every(seconds=30)
async def send_data():
    aum_server = AUMServer()
    aum_server.send_payload()