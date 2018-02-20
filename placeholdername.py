# -*- coding: utf-8 -*-

import codecs
import json
from collections import Counter
import nltk
import random
from nltk.probability import ConditionalFreqDist
from nltk import TweetTokenizer

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
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
            bigram = nltk.ngrams(tknz_lines,2)
        cfd=ConditionalFreqDist([(tuple(a), b) for *a,b in bigram])
        seed=["The"]
        for i in range(100):
            seed.append(random.choice(list(cfd[tuple(seed[-1:])].keys())))
        return seed
        print(seed)
        return
    
    def Trigrams(self,filename):
        self._filename = filename
        with codecs.open("twitterdata/"+self._filename+".txt","r","utf-8") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
        emptylist=[]
        maxhistory = 3
        for i in range(2, maxhistory+1):
            emptylist+=nltk.ngrams(tknz_lines, i)
        cfd=ConditionalFreqDist([(tuple(a), b) for *a,b in emptylist])       
        seed=["The"]
        for i in range(100):
            seed.append(random.choice(list(cfd[tuple(seed[-1:])].keys())))
        return seed
        print(seed)
        return
    
    def TextMostCommon(self,filename):
        self._filename = filename
        with codecs.open("twitterdata/"+self._filename+".txt","r","utf-8") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
            n = int(input("Choose an N for the amount of most common: "))
            self._mostcommon = Counter(tknz_lines).most_common(n)
        return self._mostcommon
    
    def TextTotalCounts(self,filename):
        self._filename = filename
        with codecs.open("twitterdata/"+self._filename+".txt","r","utf-8") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
            self._totalcount = len(tknz_lines)
        return self._totalcount
    
    
#WriteTweetTxtFile("amager")
#bigrams(city)
#    text = tweets[]["text"]
#    gram = nltk.ngrams(text,2)
#        pprint(data)
#        condition_pairs = (((w0, w1) for w0, w1 in gram))
#        dist = nltk.ConditionalFreqDist(condition_pairs)
