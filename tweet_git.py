#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "Evil tweet from an evil machine"

apiKey = 'your api key'
apiSecret = 'your api secret'
accessToken = 'your access token'
accessTokenSecret = 'your access token secret'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
