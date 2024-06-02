We are using mocking and the joke files have been split as such to show where we need to reference the 'get_joke' from.

It needs to reference the module where it is CALLED not DEFINED.

Hence we use @patch("src.joke_mock.joke.get_joke") and not @patch("src.joke_mock.api_joke.get_joke") as get_joke is called in joke.py not api_joke.py where it is defined:


def len_joke() -> int:
    """get length"""
    the_joke = get_joke() # called in joke.py
    return len(the_joke)