"""Unit Test: """

import pytest
import requests
import responses
from ipcheck.cidrdata import get_cidr_data


# custom class to be the mock return value of requests.get()
class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

    @staticmethod
    def raise_for_status():
        pass


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """requests.get() mocked to return {"mock_key": "mock_response"}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


# test uses the custom fixture mock_response instead of monkeypatch directly
def test_get_cidr_data(mock_response):

    result = get_cidr_data("https://testurl")
    assert result["mock_key"] == "mock_response"


@responses.activate
def test_get_cidr_data_connection_error():

    responses.add(responses.GET, "https://testurl", body=requests.ConnectionError())
    assert get_cidr_data("https://testurl") is False


@responses.activate
def test_get_cidr_data_timeout():

    responses.add(responses.GET, "https://testurl", body=requests.Timeout())
    assert get_cidr_data("https://testurl") is False


@responses.activate
def test_get_cidr_data_http_error():

    responses.add(responses.GET, "https://testurl", body=requests.HTTPError())
    assert get_cidr_data("https://testurl") is False


@responses.activate
def test_get_cidr_data_exception():

    responses.add(responses.GET, "https://testurl", body=Exception)
    assert get_cidr_data("https://testurl") is False
