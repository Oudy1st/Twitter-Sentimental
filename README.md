# Twitter-Sentimental-categorization

# Introduction
  This project is created to test basic text sentimental and categorization. So, I scrapped 1000 tweets and analyze them.

# Development
  All in python.

### Twitter Scrapping
I used Tweepy library to scrap some tweets with a keyword.

### Sentimental
I use Textblob library which has the sentiment method.

### Categorization
I use Textblob library to train 5 classifiers and use them jointly for multi-classification, categorize.



# Twitter Sentimental
  tweet_sentimental.py
  
  Scrapping and sentimental Steps: 
  1. Set up twitter's keys and tokens from the Twitter Dev Console.
  2. Set up your keyword, target date (start scrapping), number tweets and retweet flag.
  3. Set up your output CSV file.
  4. Run tweet_sentimental.py, which call twitter API and then create a list of tweets with their sentimental, can observe at get_tweets().
  
# Categorization
  Training Categorize Model.py
  tweet_categorize.py
  
  I need to create a model for multi-classification. So, I need to have a dataset which contains text and label.
  
  Dataset Acquired Steps:
  1. Use twitter scrapping to scrap tweets with hashtag sport, tech, government&politic, education, and business.
  2. Use Textblob library to train one-vs-all classifications for each category.
  3. Save them with pickle library.
  
  Categorize Steps:
  1. Load the models.
  2. Load the dataset and classify it with all classifiers.
  3. Normalize the results and select the highest probability.



# Result (demo)
  I scrapped 1000 tweets with #bbcnews since 01-06-2019. Then, I categorized and sentiments them.
As a result, 40% of tweets are about politic with 3 times positive than negative. Then, 25% of them is about a business which a bit more negative than positive. So, others are education (8%), tech (1%) and no sport.
