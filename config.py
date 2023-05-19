import os

from dotenv import load_dotenv
load_dotenv()


# Define variables
USER = os.environ.get('USER')

CRON_TIME = os.environ.get('CRON_TIME')

TWITTER_BEARER = os.environ.get('TWITTER_BEARER')

TWITTER_API_KEY=(
    os.environ.get('TWITTER_API_KEY'),
    os.environ.get('TWITTER_API_KEY_SECRET')
)

TWITTER_ACCESS_TOKEN=(
    os.environ.get('TWITTER_ACCESS_TOKEN'),
    os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
)

SCRAPING_URL = os.environ.get('SCRAPING_URL')

TEAM = os.environ.get('SCRAPING_TEAM')

MESSAGES = {
    "error-scrapping": f"No se pudo determinar si hoy juega {TEAM} :(",
    "plays": f"HOY JUEGA {TEAM}",
    "doesnt-play": f"HOY NO JUEGA {TEAM}"
}

