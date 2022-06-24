"""tests if CIDR data webpage content has an ipv4 key"""

import requests


def test_check_data_webpage_ipv4_key():
    """check the content has ipv4 key"""

    response = requests.get("https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix")
    json_response = response.json()
    assert "ipv4" in json_response["data"]["resources"]
