"""Twitter"""
import os
import twitter  # pip install python-twitter

URL = "http://miketwo.net/learn/mocks"


def tweet(api, message):
    """Test"""
    if len(message) > 40:
        message = message.strip(",.!?")
    if len(message) > 40:
        message = message.replace("ck", "x")
        message = message.replace("ex", "x")
    if len(message) > 40:
        message = message.replace("and", "&")
    if len(message) > 40:
        message = f"I can't be concise. {URL}"
    status = api.PostUpdate(message)
    return status


def main():
    """Test"""
    api = twitter.Api(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token_key=os.getenv("ACCESS_TOKEN_KEY"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
    )
    msg = input("What do you want to tweet? :")
    tweet(api, msg)


if __name__ == "__main__":
    main()
