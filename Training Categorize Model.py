import nltk
nltk.download('punkt')
from textblob.classifiers import NaiveBayesClassifier

import csv
import pandas as pd
import random
from itertools import groupby
from operator import itemgetter

import pickle

# df = pd.read_csv('bbc-text.csv', delimiter=',')
# items = [(x[1],x[0]) for x in df.values]

# df = pd.read_csv('twitter_scrapping_labeled100.csv', delimiter=',')
# items = [(x[1],x[2]) for x in df.values][:245]

category = ["tech", "education", "politic", "sport", "business"]
items = []
for c in category:
    df = pd.read_csv("{}.csv".format(c), delimiter=',')
    rows = [x[1] for x in df.values]
    print(len(rows))
    for row in rows:
        items.append((row, c))
    

sortkeyfn = itemgetter(1)
items.sort(key=sortkeyfn)

result = {}
for key,valuesiter in groupby(items, key=sortkeyfn):
    result[key] = list(v[0] for v in valuesiter)

    
    

cl_list = []
cl_name = []


for key in result.keys():
    train = []
    test = []
    cl_name.append(key)
    textList = result[key]
    random.shuffle(textList)
    train_size = 0.9
    train_index = int(len(textList)*train_size)
    #append base label
    for text in textList[:train_index]:
        train.append((text, "pos"))
    for text in textList[train_index:]:
        test.append((text, "pos"))
    
    #append other label
    for other_key in result.keys():
        if other_key != key:
            textList = result[other_key]
            random.shuffle(textList)
            train_size = 0.9
            train_index = int(len(textList)*train_size)
            #append other label
            for text in textList[:train_index]:
                train.append((text, "neg"))
            for text in textList[train_index:]:
                test.append((text, "neg"))
        
    cl = NaiveBayesClassifier(train)
    accuracy = cl.accuracy(test)
    print("class :{} train:{} test:{} acc:{}".format(key, len(train), len(test), accuracy))
    cl_list.append(cl)
    




#save model
object = cl_list
file = open('tweet-categorize-multiclass-array.obj','wb')
pickle.dump(object,file)