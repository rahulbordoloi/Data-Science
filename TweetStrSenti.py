import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import time

class serverRequest():
	def __init__(self):                 # the following values will be hidden for security reasons
		consumer_key = ''
		consumer_secret = ''
		access_token = ''
		access_token_secret = ''

		try:
			self.auth = OAuthHandler(consumer_key, consumer_secret)
			self.auth.set_access_token(access_token, access_token_secret)
			self.api = tweepy.API(self.auth)
		except:
			print("Error: Server Request Authentication Failed")

	def clean_tweets(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

	def get_clean_tweets(self, tweet):
		analysis = TextBlob(self.clean_tweets(tweet))
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'

	def get_tweets(self, query, count = 100):
		tweets = []

		try:
			fetched_tweets = self.api.search(q = query, count = count)

			for tweet in fetched_tweets:
				parsed_tweet = {}

				parsed_tweet['text'] = tweet.text
				parsed_tweet['sentiment'] = self.get_clean_tweets(tweet.text)

				if tweet.retweet_count > 0:
					if parsed_tweet not in tweets:
						tweets.append(parsed_tweet)
					else:
						tweets.append(parsed_tweet)
			return tweets
			
		except tweepy.TweepError as e:
			print("Twitter Error :" + str(e))

def main():
	api = serverRequest()
	tweets = api.get_tweets(query = 'Donald Trump', count = 200)
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
	print("Positive Tweet Percentage : {} %".format(100*len(ptweets)/len(tweets)))
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
	print("Neutral tweets percentage: ")
	print(100 * (len(tweets) - len(ntweets) - len(ptweets))/len(tweets)) 
	print('\n')

if __name__ == "__main__":
	main()
    #time.sleep(5.0 - ((time.time() - starttime)%5.0))
    
    
"""O/P - 
Positive Tweet Percentage : 60.43956043956044 %
Negative tweets percentage: 13.186813186813186 %
Neutral tweets percentage: 
26.373626373626372
"""
