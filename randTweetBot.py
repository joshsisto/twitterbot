#!/usr/bin/env python

import tweepy
import time
import sys
import os

from random import randint

argfile = str(sys.argv[1]) #Path for txt file

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

if __name__ == "__main__":

    while True:
        with open(argfile) as book:
            lines = book.readlines()
            rand_line_num = randint(0, len(lines) - 1)
            line = lines[rand_line_num]
            api.update_status(line)
            time.sleep(180)  # Tweets a random sentence every 3 minutes
