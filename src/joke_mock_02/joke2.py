"""Joke"""


from src.joke_mock_02.api_joke2 import get_joke2


def len_joke2() -> int:
    """get length"""
    the_joke2 = get_joke2()
    print("in joke2.py")
    return len(the_joke2)
