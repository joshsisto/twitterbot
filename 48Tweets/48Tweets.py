import tweepy
import time
import numpy as np
from credentials import *
from FortyEightLawsDictionary import *
from ThirtyThreeStrats import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

l = laws_list
tts_list = strats_list

np_l = np.array(l)
np_s = np.array(strats_list)

## https://stackoverflow.com/questions/18854620/whats-the-best-way-to-split-a-string-into-fixed-length-chunks-and-work-with-the
## create a definition to chunk strings into a specified size. Going to use to stay under Twitters character limit
def chunkstring(string, length) :
    return (string[0+i:length+i] for i in range(0, len(string), length))

if __name__ == '__main__':

    while True:

        ## tweetLaw function takes input of Law number and then tweets the law
        def tweetLaw(lawnumber):
            law_and_title = (np_l[ lawnumber, 0] + '\n' + np_l[lawnumber, 1])
            np_l_law = (np_l[lawnumber, 2])
            chunky_list = list(chunkstring(np_l_law, 140))
            api.update_status(law_and_title)
            time.sleep(1)
            for chunk in chunky_list:
                api.update_status(chunk)
                time.sleep(1)

        ## tweetStrat function takes input of strat_number and tweets a strategy
        def tweetStrat(strat_number):
            strat_and_title = (np_s[strat_number, 0] + '\n' + np_s[strat_number, 1] + '\n' + np_s[strat_number, 2])
            np_s_strat = (np_s[strat_number, 3])
            chunky_strat = list(chunkstring(np_s_strat, 140))
            api.update_status(strat_and_title)
            for chunk in chunky_strat:
                api.update_status(chunk)
                time.sleep(1)

        ## Tweet a law and strategy
        for vals in range(0, 48):
            if vals <= 32:
                tweetLaw(vals)
                time.sleep(7200)
                tweetStrat(vals)
                time.sleep(7200)
            else:
                tweetLaw(vals)
                time.sleep(7200)
