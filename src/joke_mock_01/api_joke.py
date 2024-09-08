"""Get joke request"""

import requests


def get_joke() -> str:
    """get a joke"""

    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url, timeout=30)

    if response.status_code == 200:
        joke = response.json()["value"]
    else:
        joke = "NO_JOKE"
    print("in api_joke.py")
    return joke


# print(len_joke())
