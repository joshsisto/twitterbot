import tweepy
from time import sleep
import numpy as np
from credentials import *
from FortyEightLawsDictionary import *

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

# my_file = open('48laws.txt','r')
# file_lines = my_file.readlines()
# my_file.close()
#
# for line in file_lines:
# # Add try ... except block to catch and output errors
#     try:
#         print(line)
#         if line != '\n':
#             api.update_status(line)
#         else:
#             pass
#     except tweepy.TweepError as e:
#         print(e.reason)
#     sleep(5)



l = laws_list

## https://stackoverflow.com/questions/18854620/whats-the-best-way-to-split-a-string-into-fixed-length-chunks-and-work-with-the
## create a definition to chunk strings into a specified size. Going to use to stay under Twitters character limit
def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

## Creates a numpy array and then creates a variable with the definition of Law 1
np_l = np.array(l)
np_l_one = (np_l[0, 2])
## Creates a variable and chunks the definition of Law 1 into 120 Character chunks
chunk_l = list(chunkstring(np_l_one, 120))
print(chunk_l)

## This prints Law 1 Never Outshine the Master and then prints the Law
np_l = np.array(l)
print(np_l[0, 0] + ' ' + np_l[0, 1])
print(np_l[0, 2])

## This prints all of the laws (the first item of each list)
np_l = np.array(l)
print(np_l[:, 0])

## This prints Law 1
np_l = np.array(l)
print(np_l[0, 0])

## This will print each law out
for s in l:
    print(*s)
