import app.twitter as twitter
import app.scraping as scraping

def run():
    try:
        api = twitter.connect_api()
        if (api == None):
            raise Exception('Error with the API')

        message = scraping.run()
        api.create_tweet(text=message)
    except Exception as ex:
        print(ex)


if (__name__ == '__main__'):
    run()
