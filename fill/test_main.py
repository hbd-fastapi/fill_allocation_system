import pytest

from main import FillServer

fill_server = FillServer()


def test_prepare_payload():
    payload = fill_server.prepare_payload()
    print(payload)

    assert "stock_ticker" in payload
    assert "price" in payload
    assert "quantity" in payload
