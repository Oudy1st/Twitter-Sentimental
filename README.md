# Twitter-Sentimental-categorization

# Introduction
  This project is created for test basic text sentimental and categorization. So, I scrapped 1000 tweets and analyse them.

# Development
  All in python.

### Twitter Scrapping
I use tweepy library to scrap some tweets with keyword.

### Sentimental
I use textblob library which has sentiment method.

### Categorization
I use textblob library to train 5 classifiers and use them joinly for multi-classification, categorize.



# Twitter Sentimental
  tweet_sentimental.py
  
  Scrapping and sentimental Steps: 
  1. Set up twitter's keys and tokens from the Twitter Dev Console.
  2. Set up your keyword, target date (start scrapping), number tweets and retweet flag.
  3. Set up your output csv file.
  4. Run tweet_sentimental.py, which call twitter API and then create list of tweets with their sentimental, can observe at get_tweets().
  
# Categorization
  Training Categorize Model.py
  tweet_categorize.py
  
  I need to create the model for multi-classification. So, I need to have dataset which contain text and label.
  
  Dataset Acquired Steps:
  1. Use twitter scrapping to scrap tweets with hashtag sport, tech, government&politic, education and business.
  2. Use textblob library to train one-vs-all classifications for each category.
  3. Save them with pickle library.
  
  Categorize Steps:
  1. Load the models.
  2. Load the dataset and classify it with all classifiers.
  3. Normalize the results and select the highest probability.


