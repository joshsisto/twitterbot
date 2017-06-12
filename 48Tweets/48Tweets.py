import tweepy
import time
import numpy as np
from credentials import *
from FortyEightLawsDictionary import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

l = laws_list
np_l = np.array(l)

if __name__ == '__main__':
    while True:

            
        ## https://stackoverflow.com/questions/18854620/whats-the-best-way-to-split-a-string-into-fixed-length-chunks-and-work-with-the
        ## create a definition to chunk strings into a specified size. Going to use to stay under Twitters character limit
        def chunkstring(string, length) :
            return (string[0+i:length+i] for i in range(0, len(string), length))

        ## tweetLaw function takes input of Law number and then tweets the law
        def tweetLaw(lawnumber):
            law_and_title = (np_l[ lawnumber, 0 ] + '\n' + np_l[lawnumber, 1])
            np_l_law = (np_l[lawnumber, 2])
            chunky_list = list(chunkstring(np_l_law, 140))
            api.update_status(law_and_title)
            time.sleep(1)
            for chunk in chunky_list:
                api.update_status(chunk)
                time.sleep(1)

        ## Tweet a law and wait 4 hours to tweet again
        for Laws in range(0 , 48):
            tweetLaw(Laws)
            time.sleep(14400)
