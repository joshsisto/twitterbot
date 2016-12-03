from __future__ import absolute_import, print_function
from datetime import datetime, timedelta
from json import loads
from urllib import urlopen

import tweepy
import time

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps

#api.update_status(status='C3P0 is not evil! R2D2 is questionable!')

#Bitcoin

def get_bitcoin_price(endpoint):
    req = urlopen('http://api.coindesk.com/v1/bpi/{}'.format(endpoint))
    return loads(req.read())


def get_current_btc_price():
    return get_bitcoin_price('currentprice.json')['bpi']['USD']


def get_last_years_btc_price():
    last_year = (datetime.now() - timedelta(days=366)).strftime('%Y-%m-%d')
    endpoint = 'historical/close.json?start={0}&end={0}'.format(last_year)
    return get_bitcoin_price(endpoint)['bpi']


if __name__ == '__main__':

    while True:

        current_price = get_current_btc_price()
        pri = ('Current BTC Price: ${rate_float:.2f} USD '.format(**current_price))

        last_years_price = get_last_years_btc_price()
        pri2 = ('BTC Price on {}: ${:.2f} USD'.format(*last_years_price.items()[0]))

        api.update_status(pri + pri2 + ' #bitcoin')     # update status
        time.sleep(86400)                               # wait 24 hours

# End of Bitcoin
