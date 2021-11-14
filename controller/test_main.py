import pytest

from main import ControllerServer

controller_server = ControllerServer()


def test_split_stocks():
    
    accounts = {'account1': 36, 'account2': 10, 'account3': 54}
    fills = {'stock_ticker': 'WOM', 'price': 32.76, 'quantity': 91}


    assert len(controller_server.split_stocks()) == 3

