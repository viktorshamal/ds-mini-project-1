# -*- coding: utf-8 -*-

import codecs
import json
from collections import Counter
import nltk
import random
from nltk.probability import ConditionalFreqDist
from nltk import TweetTokenizer
import re

#from pprint import pprint
#from string import punctuation
#from nltk.corpus import stopwords
#from nltk import word_tokenize
#from math import log

class placeholder():
    
    def __init__(self,filepath):
        self._filepath= filepath
        self._counts = 0
        self._totalcount = 0

    def WriteTweetTxtFile(self):
#        self._filepath = filepath
        with codecs.open(self._filepath+".json","r","utf-8") as f:    
            tweets = json.load(f,encoding = "utf-8")
            with open(self._filepath+".txt","w") as file:
                for i in range(len(tweets)):
                    file.write(tweets[i]["text"]+"\n")
                    
    def Ngrams(self):
#        self._filepath = filepath
        name = re.findall("\w+$",self._filepath)
        with codecs.open(self._filepath+".txt","r","utf-8") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
        emptylist=[]
        maxhistory = int(input("Choose n for ngram, preferably 2 or 3: "))
        for i in range(2, maxhistory+1):
            emptylist+=nltk.ngrams(tknz_lines, i)
        cfd=ConditionalFreqDist([(tuple(a), b) for *a,b in emptylist])       
        seed=[str(name[0])]
        for i in range(100):
            for j in range(maxhistory-1,0,-1):
                if tuple(seed[-j:]) in cfd:
                    valuesum=sum(cfd[tuple(seed[-j:])].values())
                    value = random.randint(0,valuesum)
                    for key in cfd[tuple(seed[-j:])].keys():
                        value-=cfd[tuple(seed[-j:])][key]
                        if value <= 0:
                            seed.append(key)
                            break
                    break
                else:
                    continue
        return seed
        print(seed)
        return
    
    def TextMostCommon(self):
#        self._filepath = filepath
        with codecs.open("twitterdata/"+self._filename+".txt","r","utf-8") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
            n = int(input("Choose an N for the amount of most common: "))
            self._mostcommon = Counter(tknz_lines).most_common(n)
        return self._mostcommon
    
    def TextTotalCounts(self):
#        self._filepath = filepath
        with codecs.open("twitterdata/"+self._filepath+".txt","r","utf-8") as f:
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
