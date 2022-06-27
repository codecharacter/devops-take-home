import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError

URL = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"


def get_cidr_data():
    """Get all data from webpage."""

    print("Checking if CIDR data on webpage is available, then requesting data...")
    print("   > there's a lot of data, it may take a minute (insert: elevator theme music)")

    try:

        response = requests.get(URL)
        response.raise_for_status()  # Assert that there were no errors

    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}\nPlease try again.")
    except Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}\nPlease try again.")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}\nPlease try again.")
    except Exception as err:
        print(f"Other error occurred: {err}\nPlease try again.")
    else:
        print("CIDR data successfully captured.")
        json_response = response.json()
        return json_response['data']['resources']['ipv4']
