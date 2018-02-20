# -*- coding: utf-8 -*-

import codecs
import json
from collections import Counter
import nltk
import random
from nltk.probability import ConditionalFreqDist

#from pprint import pprint
#from string import punctuation
#from nltk.corpus import stopwords
#from nltk import word_tokenize
#from math import log

class placeholder():
    
    def __init__(self,filename):
        self._filename= ""
        self._counts = 0
        self._totalcount = 0

    def WriteTweetTxtFile(self,filename):
        self._filename = filename
        with codecs.open("twitterdata/"+self._filename+".json","r","utf-8") as f:    
            tweets = json.load(f,encoding = "utf-8")
            with open("twitterdata/"+self._filename+".txt","w") as file:
                for i in range(len(tweets)):
                    file.write(tweets[i]["text"]+"\n")
                    
    def Bigrams(self,filename):
        self._filename = filename
        with codecs.open("twitterdata/"+self._filename+".txt","r","utf-8") as f:
            document = f.read()    
            gram = nltk.ngrams(document,2)
        cfd=ConditionalFreqDist([(tuple(a), b) for *a,b in gram])
        seed=["amager"]
        def generate(seed, cfd, maxcount=100):
            for i in range(maxcount):
                seed.append(random.choice(list(cfd[tuple(seed[-1:])].keys())))
            return seed
        print(generate(seed, cfd))
        return
    
    def TextCount(self,filename):
        self._filename = filename
        with codecs.open("twitterdata/"+self._filename+".txt","r","utf-8") as f:
            lines = f.read()
            self._counts = Counter(lines)
        return self._counts
    
    def TextTotalCounts(self,filename):
        self._filename = filename
        with codecs.open("twitterdata/"+self._filename+".txt","r","utf-8") as f:
            self._totalcount = len(f)
        return self._totalcount
    
    
#WriteTweetTxtFile("amager")
#bigrams(city)
#    text = tweets[]["text"]
#    gram = nltk.ngrams(text,2)
#        pprint(data)
#        condition_pairs = (((w0, w1) for w0, w1 in gram))
#        dist = nltk.ConditionalFreqDist(condition_pairs)
