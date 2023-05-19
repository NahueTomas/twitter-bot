import tweepy
from config import TWITTER_API_KEY, TWITTER_ACCESS_TOKEN, TWITTER_BEARER

def connect_api():
    try:
        api = tweepy.Client(
            bearer_token=TWITTER_BEARER,
            access_token=TWITTER_ACCESS_TOKEN[0],
            access_token_secret=TWITTER_ACCESS_TOKEN[1],
            consumer_key=TWITTER_API_KEY[0],
            consumer_secret=TWITTER_API_KEY[1]
        )
        print("Authenticated!")
        return api
    except Exception as err:
        print(err)
        print("Error during Authentication")
