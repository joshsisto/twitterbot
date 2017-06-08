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



# print(laws_list)
# print(laws_list[0:47])

l = laws_list




# ## This prints Law 1
# np_l = np.array(l)
# print(np_l[0,0])

# ## This will print each law out
# for s in l:
#     print(*s)
