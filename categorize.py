
import pickle
import csv
import pandas as pd
from operator import itemgetter


#load model
pickle_in = open("tweet-categorize-multiclass-array.obj","rb")
cl_list = pickle.load(pickle_in)
cl_name = ["tech", "education", "politic", "sport", "business"]



def classify(text):
    prob_list = []
    for cl in cl_list:
    #     cl.show_informative_features(5)
        prob_dist = cl.prob_classify(text)
    #     print(prob_dist.max())
        pos = prob_dist.prob("pos")
        neg = prob_dist.prob("neg")
        prob_list.append(pos)
    
    normalize_prob = [round(x/sum(prob_list),3) for x in prob_list]
#     print(normalize_prob)
    max_index, max_value = max(enumerate(normalize_prob), key=itemgetter(1))
    return cl_name[max_index]



df = pd.read_csv('twitter_scrapping.csv', delimiter=',')
tweets = [(x[0],x[1],x[2],x[3],x[4]) for x in df.values]
# opening a csv file
csvFile = open('twitter_categorized.csv', 'a')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['create at','tweet', 'categorize', 'sentiment', 'retweet', 'favorite'])

    
for tweet in tweets:
    classify_result = classify(tweet[1])
#     print([tweet[1],classify_result])
    csvWriter.writerow([tweet[0], tweet[1], classify_result, tweet[4], tweet[2], tweet[3]])
    
    