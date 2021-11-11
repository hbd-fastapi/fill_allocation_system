"""
AUM Server (ASSETS UNDER MANAGEMENT)

- sends account splits every 30 seconds
- payload of the split: 
    {
        "account1": <random>,
        "account2": <random>,
        "account3": <random>
    }

"""

import time
import json
import random
import requests


def split_percentages(count):
    """Returns tuple with percentages depending on the number of accounts"""
    
    percentages = []
    for i in range(count):
        value = random.randint(0, 100)
        current_sum = sum(percentages)
        
        if current_sum+value <= 100 and i < count-1:
            percentages.append(value)
        else:
            percentages.append(100-current_sum)

    return percentages


def prepare_payload(count):
    """Prepares payload to send"""
    
    payload = {}
    percentages = split_percentages(count)

    for i in range(count):
        payload[f'account{i+1}'] = percentages[i]

    return [payload]


def connection(url):
    with requests.Session() as s:
        while True:
            accounts = random.randint(1, 4)
            # payload = {"data": prepare_payload(accounts)}

            payload = {'data': [{'account_name': 'Account_1', 'percentage': 93}, {'account_name': 'Account_2', 'percentage': 7}]}

            r = s.post(url=url, json=payload)

            time.sleep(2)



if __name__ == "__main__":
    connection('http://controller:8001/accounts/')

