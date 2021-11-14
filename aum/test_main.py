import pytest

from main import AUMServer

aum_server = AUMServer()


def test_split_percentages():
    assert len(aum_server.split_percentages(3)) == 3
    assert sum(aum_server.split_percentages(3)) == 100
    assert len(aum_server.split_percentages(4)) == 4
    assert sum(aum_server.split_percentages(4)) == 100


def test_prepare_payload():
    payload = aum_server.prepare_payload()
    percentage = sum(payload.values())

    assert "account1" in payload  
    assert "account2" in payload  
    assert percentage == 100  

