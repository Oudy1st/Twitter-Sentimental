import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import csv


class TwitterClient(object): 
    '''
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = 'l7oHZ1s1FoJLLpB3b8dlnhuSg'
        consumer_secret = 'A8X8MbFrMmAUscEOB18qs0ygwp9h3CDAMiLipJgs7ryvyhEA8q'
        access_token = '487149209-OXfcn2GvgEDjqpkrspM0oJDkbCNvEvNVeHbHzpfe'
        access_token_secret = '6sqXM7tZz0nLdL8tB4v9LtySe5u0DlJELxg3zt1NlK2lQ'

        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 

    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
#         return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
        return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet).split())

    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    def get_tweets(self, query, start, count = 10, allow_retweet = True): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 

        try: 
#             # call twitter api to fetch tweets 
#             fetched_tweets = self.api.search(q = query, count = count) 
            # receiving keyword you want to search for
            fetched_tweets = tweepy.Cursor(self.api.search, q=query, lang="en", since=start).items(count)
            # parsing tweets one by one 
            count = 0
            for tweet in fetched_tweets: 
                count = count+1
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
#                 print(tweet.text)
                if not (allow_retweet == False and tweet.text.startswith('RT ')):
                    # saving text of tweet 
                    parsed_tweet['text'] = tweet.text 
                    # saving create date of tweet
                    parsed_tweet['created_at'] = tweet.created_at
                    # saving retweet of tweet
                    parsed_tweet['retweet'] = tweet.retweet_count
                    # saving favorite of tweet
                    parsed_tweet['favorite'] = tweet.favorite_count
                    # saving sentiment of tweet 
                    parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

                    # appending parsed tweet to tweets list 
                    if tweet.retweet_count > 0: 
                        # if tweet has retweets, ensure that it is appended only once 
                        if parsed_tweet not in tweets: 
                            tweets.append(parsed_tweet) 
                    else: 
                        tweets.append(parsed_tweet) 

            print("get tweets : {}".format(count))
            # return parsed tweets 
            return tweets 

        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 
            
def saveCSV(fileName, tweet_list):
    # opening a csv file
    csvFile = open(fileName, 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['created at', 'tweet', 'retweet', 'favorite', 'sentiment'])
    for tweet in tweet_list:
        csvWriter.writerow([tweet["created_at"], tweet["text"], tweet["retweet"], tweet["favorite"], tweet["sentiment"]])
        
def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets(query = '#bbcnews', start = '2019-01-01', count = 1000, allow_retweet = False) 
    print(len(tweets))
    saveCSV('twitter_scrapping_bbcnews.csv',tweets)


if __name__ == "__main__":
    main()
