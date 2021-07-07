#!/usr/bin/env python3

import tweepy
import logging
import pandas as pd
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Defines a function to collect tweets and store them in a readable format
def gather_info(api, keywords, tweet_count):
    logger.info("Scanning tweets...")
    # Collects tweets using tweepy and the Twitter API
    tweets = tweepy.Cursor(api.search,
                           q=keywords,
                           lang="en").items(tweet_count)
    # Returns the username, tweet text, and tweet creation time...
    tweet_data = [[tweet.user.screen_name, tweet.text, tweet.created_at] for tweet in tweets]

    # Creates a pandas DataFrame out of the results...
    tweet_df = pd.DataFrame(data=tweet_data,
                            columns=['User', 'Text', 'Time Created'])
    # Prints the newly-created DataFrame
    print(tweet_df)


def main():
    api = create_api()
    gather_info(api, "$WKHS", 10)


if __name__ == "__main__":
    main()
