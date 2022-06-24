"""Tests if CIDR data webpage is accessible"""

import requests


def test_check_data_webpage_status_code():
    """Check the status code of data webpage"""

    response = requests.get("https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix")
    assert response.status_code == 200
