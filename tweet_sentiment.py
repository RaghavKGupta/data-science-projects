import tweepy
from textblob import TextBlob


consumer_key= 'MOCDWsnhTg3grUgTFBdS3Zn7V'
consumer_secret= 'KUO9JQxbJn0ahWUYrpT9YWihAw1CToTbP9reBkvMCOUAKAL1xX'

access_token='1294346384-llUpXqjfv2hqXDU5H9Rot3j4DTyNjgOfQwhaEmZ'
access_token_secret='6GbPTnLohxvWAGmayjK6rzGQ1WzgUBQ8A3c9RtAufG5Wi'

authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticate.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticate)


tweets = api.search('Trump')


for tweet in tweets:
    print(tweet.text)

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")