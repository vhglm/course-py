import pytest

from gww.client import Client


@pytest.fixture
def test_client():
    return Client()

def test_get_reservoirs(test_client):
    reservoir_json = test_client.reservoirs.get(90554)
    # assert valid geojson
    assert reservoir_json["id"] == 90554
    assert reservoir_json.get("properties") is not None
    assert reservoir_json.get("geometry") is not None
