# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:39:16 2018

@author: jeppe
"""
import afinn
import codecs
from sys import argv
import glob
import os

af = afinn.Afinn(language="da")
path = 'infomedia_data/'
text_files = glob.glob(path + "*.txt")
results = []
cities = ["amager","indreby","nørrebro","torvehallerne","valby","vesterbro","østerbro"]
print(text_files)
for tf in text_files:
    path = os.path.splitext(tf)[0]
#    print(tf)
    with codecs.open(tf,encoding = "latin-1" ) as f:
        text = f.read()
        score = af.score(text)
        results.append(score)
#        with codecs.open(articles,encoding = "latin-1") as f:
print(results)
with open("twitterdata/sentiment_results/results.txt","w") as f:
    for result in results:
        f.write(str(result)+"\n")
#print(sentimentscore())