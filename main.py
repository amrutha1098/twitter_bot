# This is a sample Python script to develop a twitter bot


#  using tweetpy lib ( documentation -> https://docs.tweepy.org/en/latest/ )
import tweepy
import time
#  defining the twitter users keys
api_key = ""
api_secret = ""
access_token = ""
access_secret_key_token = ""
bearer_token = ""

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret_key_token)
api = tweepy.API(auth)

# def functions/methods
# get the latest seen / responded tweet id
def get_latest_tweet_id():
    f = open("latest_tweet_id.txt", "r")
    return (f.read())

# store latest in db / file
def store_latest_tweet_id(id):
    f = open("latest_tweet_id.txt","w")
    f.write(str(id))

# get all the recent tweets tagged to the dev twitter account
def get_tweets_and_respond():
    latest_id = get_latest_tweet_id()
    mentions = api.mentions_timeline(since_id=latest_id)
    for mention in mentions[::-1]:
        store_latest_tweet_id(mention.id)
        if '#helloamrutha' in mention.text.lower():
            api.update_status('@' + mention.user.screen_name + ' hello back at you ' + mention.user.name , in_reply_to_status_id=mention.id)
while True:
    get_tweets_and_respond()
    time.sleep(20)


# to do add logger statements