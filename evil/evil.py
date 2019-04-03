import tweepy
from credentials import *
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
user = api.me()
print(f'Activating Twitter Bot: {user.name}')


def update_status(twitter_status):
    api.update_status(status=twitter_status)


def follow_back():
    follow_back = input('Would you like to follow everyone who follows you? Y/N: ').upper()
    if follow_back == 'Y':
        for follower in tweepy.Cursor(api.followers).items():
            print(follower)
            follower.follow()


def get_user_tweets():
    search = input('What Twitter username would you like to search?: ')
    numberOfTweets = int(input(f'How many tweets would you like to lookup for {search}?: '))

    user_tweets = api.user_timeline(screen_name=search, count=numberOfTweets, include_rts=False, tweet_mode='extended')

    for tweet in user_tweets:
        print(tweet.full_text)


def reply_to_tweets(t_user, phrase, numberOfTweets):
    for tweet in tweepy.Cursor(api.search, t_user).items(numberOfTweets):
        try:
            # Reply
            print('\nTweet by: @' + tweet.user.screen_name)
            print('ID: @' + str(tweet.user.id))
            tweetId = tweet.user.id
            username = tweet.user.screen_name
            # api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
            print(username)
            print("Replied with " + phrase)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


def fav_retweet_follow(t_user, numberOfTweets):
    for tweet in tweepy.Cursor(api.search, t_user).items(numberOfTweets):
        try:
            tweet.favorite()
            tweet.retweet()
            tweet.user.follow()
            print(f'Liked and retweeted {tweet}')
            print(f'Followed {tweet.user.follow}')

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


def retweet_hashtag():
    for tweet in tweepy.Cursor(api.search, q=('#Bitcoin OR #Python OR #Django OR #raspberrypi OR #Triathlon -filter:retweets'), lang='en').items(10):
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print(tweet.text)
            time.sleep(5)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


retweet_hashtag()

# fav_retweet_follow('joshsisto', 10)
# get_user_tweets()
# follow_back()
# reply_to_tweets('joshsisto', 'boom', 10)


