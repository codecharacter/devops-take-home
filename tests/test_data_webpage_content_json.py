"""Tests if CIDR data webpage content type is JSON"""

import requests


def test_check_data_webpage_content_type_json():
    """Check the content is JSON from data webpage"""

    response = requests.get("https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
