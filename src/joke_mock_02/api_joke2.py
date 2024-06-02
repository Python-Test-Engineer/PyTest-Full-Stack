"""Get joke request and add Exceptions"""

import requests


def get_joke2() -> str:
    """get a joke"""

    url = "https://api.chucknorris.io/jokes/random"
    print("----------")
    print(type(requests.exceptions.Timeout))
    print("----------")
    print()
    try:
        response = requests.get(url, timeout=30)
        #  there is also response.raise_for_status()
        #  rather than checking just 200
        #  https://www.youtube.com/watch?v=RqR0AvEujrU&t=169s
        if response.status_code == 200:
            joke = response.json()["value"]
        else:
            joke = "NO_JOKE NOT 200"
        print("in api_joke2.py")
        return joke
    except requests.exceptions.Timeout:
        return "NO_JOKE NOT 200"
    except requests.exceptions.ConnectionError:
        return "NO_JOKE NOT 200"
