import unittest
from mock import Mock


import short_tweeter


class TweetTest(unittest.TestCase):
    def test_0152_example(self):
        mock_twitter = Mock()
        msg = "message"
        short_tweeter.tweet(mock_twitter, msg)
        print(mock_twitter.mock_calls)
        mock_twitter.PostUpdate.assert_called_with(msg)

    def test_0153_example2(self):
        mock_twitter = Mock()
        msg = "message!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        expected_message = "message"
        short_tweeter.tweet(mock_twitter, msg)
        print(mock_twitter.mock_calls)
        mock_twitter.PostUpdate.assert_called_with(expected_message)


if __name__ == "__main__":
    unittest.main()
