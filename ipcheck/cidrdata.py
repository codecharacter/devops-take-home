import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout


def get_cidr_data(url):
    """Get all data from webpage."""

    print("Checking........")

    try:

        response = requests.get(url)
        response.raise_for_status()  # Assert that there were no errors

    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}\nPlease try again.")
        return False
    except Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}\nPlease try again.")
        return False
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}\nPlease try again.")
        return False
    except Exception as err:
        print(f"Other error occurred: {err}\nPlease try again.")
        return False
    else:
        return response.json()
