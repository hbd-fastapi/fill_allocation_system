import pytest

from server import split_percentages, prepare_payload



def test_split_percentages():
    assert len(split_percentages(3)) == 3
    assert sum(split_percentages(3)) == 100
    assert sum(split_percentages(3)) == 100
    assert sum(split_percentages(3)) == 100
    assert sum(split_percentages(4)) == 100
    assert sum(split_percentages(5)) == 100
    assert sum(split_percentages(6)) == 100
    assert sum(split_percentages(7)) == 100


def test_prepare_payload():
    payload = prepare_payload(3)
    percentage = sum(payload.values())

    assert "account1" in payload  
    assert "account2" in payload  
    assert "account3" in payload  
    assert percentage == 100  

