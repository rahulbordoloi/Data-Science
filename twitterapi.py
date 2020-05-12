# Diving deep into Twitter API

import tweepy, json

"""Using Tweepy : Authentication Handler"""

access_token = ' '
access_token_secret = ' '
consumer_key = ' '
consumer_secret = ' '

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

"""Creation of Stream Object and to filter Tweets according to particular Keywords"""

l = MyStreamListener                              # initialise Stream Listener
stream = tweepy.Stream(auth,l)                    # create stream obj with authentication
stream.filter(track = ['clinton','trump'])        # filter tweet streams to capture data by keywords

"""Loading and Exploring Twitter Data"""

tweets_data_path = 'tweets.txt'
tweets_data = []                               # initialising empty list
tweets_file = open(tweets_data_path, 'r')      # open connection to the file
for line in tweets_file:
  tweet = json.load(line)
  tweets_data.append(tweet)
tweets_file.close()

print(tweets_data[0].keys())                   # print the keys of the 1st tweet dictionary

"""Now, we've the twitter data in a list of dictionaries, where each dictionary corresponds to a single tweet."""

import pandas as pd
df = pd.DataFrame(tweets_data, columns = ['text','lang'])              # columns - list of keys we wish to have columns of
print(df.head())

"""Studying Particular Entries (Data Analysis)"""

for i,rows in df.iterrows():                               # to analyse tweets related to clinton
  clinton+ = word_in_text('clinton',row['text'])
