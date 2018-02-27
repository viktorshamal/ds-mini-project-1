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
#from algs4.stdlib import stdio
#file = argv[1]

#def sentimentscore():
af = afinn.Afinn(language="da")
path = 'instagram/scrapefiles/'
path1 = 'instagram/scrapefiles/'
text_files = glob.glob(path + "*notrash.txt")
results = []
cities = ["amager","indreby","nørrebro",
          "torvehallerne","valby","vesterbro",
          "østerbro"]
print(text_files)
for tf in text_files:
    path = os.path.splitext(tf)[0]
#    print(tf)
    with codecs.open(tf,encoding = "latin-1" ) as f:
        text = f.read()
        score = af.score(text)
        results.append(score/(len(text)))
#        with codecs.open(articles,encoding = "latin-1") as f:
print(results)
with open(path1+"/sentiment_results/results.txt","w") as f:
    for result,city in zip(results,cities):
        f.write(str(city)+": "+str(result)+"\n")
#print(sentimentscore())