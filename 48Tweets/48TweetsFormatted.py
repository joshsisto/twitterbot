import tweepy
from time import sleep
import numpy as np
from credentials import *
from FortyEightLawsDictionary import *

l = laws_list
np_l = np.array(l)

## https://stackoverflow.com/questions/18854620/whats-the-best-way-to-split-a-string-into-fixed-length-chunks-and-work-with-the
## create a definition to chunk strings into a specified size. Going to use to stay under Twitters character limit
def chunkstring(string, length) :
    return (string[0+i:length+i] for i in range(0, len(string), length))

## Print the Law number and title, and then print the law definition formatted to 135 characters
def printTweet(lawnumber):
    print(np_l[ lawnumber, 0 ] + '\n' + np_l[lawnumber, 1])
    np_l_law = (np_l[lawnumber, 2])
    chunky_list = list(chunkstring(np_l_law, 135))
    for chunk in chunky_list:
        print(chunk)

## Print all 48 Laws formatted for Twitter
for Laws in range(0 , 48):
    printTweet(Laws)

