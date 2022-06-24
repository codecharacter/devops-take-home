"""Test transport adapter with stubbed out HTTP requests"""

import pytest
import requests


def test_url(requests_mock):
    """Testing with custom adapter"""

    requests_mock.get("https://stat.ripe.net", text="data")
    assert "data" == requests.get("https://stat.ripe.net").text
