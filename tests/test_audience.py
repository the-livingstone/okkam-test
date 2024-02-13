import urllib.parse

import pytest
from fastapi.testclient import TestClient

from tests.helpers import get_json

OVERLAP_0_33 = (
    "audience1="
    + urllib.parse.quote("Sex = 2")
    + "&audience2="
    + urllib.parse.quote("Age = 20")
)
AUDIENCE1_EMPTY = (
    "audience1="
    + urllib.parse.quote("Age > 90")
    + "&audience2="
    + urllib.parse.quote("Sex = 1")
)
AUD1_FULL_IN_AUD2 = (
    "audience1="
    + urllib.parse.quote("Age > 30")
    + "&audience2="
    + urllib.parse.quote("Age > 10")
)
AUD1_NO_OVERLAP_AUD2 = (
    "audience1="
    + urllib.parse.quote("Sex = 2")
    + "&audience2="
    + urllib.parse.quote("Age = 50")
)


def test_overlap(test_client: TestClient):
    response = get_json(test_client.get(f"/getPercent?{OVERLAP_0_33}"))
    assert round(response["percent"], 2) == 0.33


def test_audience1_empty(test_client: TestClient):
    get_json(
        test_client.get(f"/getPercent?{AUDIENCE1_EMPTY}"), status_code=422
    )


def test_aud1_full_in_aud2(test_client: TestClient):
    response = get_json(test_client.get(f"/getPercent?{AUD1_FULL_IN_AUD2}"))
    assert round(response["percent"]) == 1


def test_aud1_no_overlap_aud2(test_client: TestClient):
    response = get_json(test_client.get(f"/getPercent?{AUD1_NO_OVERLAP_AUD2}"))
    assert round(response["percent"]) == 0
