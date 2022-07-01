"""Unit Test: use of mocking for requests.get() to check JSON data retrieved."""

import pytest
import requests
import responses
from ipcheck.cidrdata import get_cidr_data


class MockResponse:
    """to be the mock return value of requests.get()."""
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}

    @staticmethod
    def raise_for_status():
        pass


@pytest.fixture
def mock_response(monkeypatch):
    """requests.get() mocked to return {"mock_key": "mock_response"}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


def test_get_cidr_data(mock_response):
    """
    GIVEN an url with JSON data
    WHEN supplied to the module's function
    THEN a successful return of valid JSON
    """
    # ARRANGE & ACT
    result = get_cidr_data("https://testurl")

    # ASSERT
    assert result["mock_key"] == "mock_response"


@responses.activate
def test_get_cidr_data_connection_error():
    """
    GIVEN an url to mock out request
    WHEN forcing a ConnectionError
    THEN successfully raises the Exception
    """
    # ARRANGE & ACT
    responses.add(responses.GET, "https://testurl", body=requests.ConnectionError())

    # ASSERT
    assert get_cidr_data("https://testurl") is False


@responses.activate
def test_get_cidr_data_timeout():
    """
    GIVEN an url to mock out request
    WHEN forcing a Timeout
    THEN successfully raises the Exception
    """
    # ARRANGE & ACT
    responses.add(responses.GET, "https://testurl", body=requests.Timeout())

    # ASSERT
    assert get_cidr_data("https://testurl") is False


@responses.activate
def test_get_cidr_data_http_error():
    """
    GIVEN an url to mock out request
    WHEN forcing an HTTPError
    THEN successfully raises the Exception
    """
    # ARRANGE & ACT
    responses.add(responses.GET, "https://testurl", body=requests.HTTPError())

    # ASSERT
    assert get_cidr_data("https://testurl") is False


@responses.activate
def test_get_cidr_data_exception():
    """
    GIVEN an url to mock out request
    WHEN forcing an Exception
    THEN successfully raises the Exception
    """
    # ARRANGE & ACT
    responses.add(responses.GET, "https://testurl", body=Exception)

    # ASSERT
    assert get_cidr_data("https://testurl") is False
