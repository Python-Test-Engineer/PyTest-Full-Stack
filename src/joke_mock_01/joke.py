"""Joke"""


from src.joke_mock_01.api_joke import get_joke


def len_joke() -> int:
    """get length"""
    the_joke = get_joke()
    print("in joke.py")
    return len(the_joke)
