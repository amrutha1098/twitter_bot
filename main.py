# This is a sample Python script to develop a twitter bot


#  using tweetpy lib ( documentation -> https://docs.tweepy.org/en/latest/ )

import tweepy


#  defining the twitter users keys

api_key = "jKHKRxYwqBjJXmqbgcwj637Cu"
api_secret = "SA8T2HsMh0tvNV644FUAfNqSE4tKwx65GZOjZ7nupM3ijqVAmP"
access_token = "1459746418734755842-IVZ9E97nOgGHYeGyM0RAU4RYIfIDKK"
access_secret_key_token = "Hoqp8379jdcJgWTT9T8FHdCixYDxrCBwazji6d2A0sWJt"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIcWVwEAAAAAL%2F7DfmypGf8kklKis0jEaTnOf30%3D6VapK1L1NKx68TdaOH5OYw3LouQ1R5T9LYorFHiL0SEGoWK7b3"


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret_key_token)

api = tweepy.API(auth)


# get all the recent tweets tagged to the dev twitter account

mentions = api.mentions_timeline()
for mention in mentions:

    if '#helloamrutha' in mention.text.lower():
        print(mention.text)
        api.update_status('@' + mention.user.screen_name + ' hello back at you ' + mention.user.name , in_reply_to_status_id=mention.id)

