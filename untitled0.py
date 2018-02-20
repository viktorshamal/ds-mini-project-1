# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:10:20 2018

@author: jeppe
"""
import codecs
import json
from placeholdername import placeholder
from nltk.tokenize import word_tokenize
from nltk import TweetTokenizer
from collections import Counter
import nltk
from nltk.probability import ConditionalFreqDist
import random


#if __name__ == "__main__":
#ph = placeholder("amager")
#    print(ph.TextCount("amager").most_common(n=20))
#    print(ph.TextTotalCounts("amager"))

byer = ["amager","indreby","nørrebro","torvehallerne","valby","vesterbro","østerbro"]
pf = placeholder("amager")
pf.Bigrams("amager")

#with codecs.open("twitterdata/amager.txt","r","utf-8") as f:
#    document = f.read()
#    tknzr = TweetTokenizer()
#    stuff =tknzr.tokenize(document)
#    
                