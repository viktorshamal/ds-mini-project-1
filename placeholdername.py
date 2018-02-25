# -*- coding: utf-8 -*-

import codecs
import json
from collections import Counter
import nltk
import random
from nltk.probability import ConditionalFreqDist
from nltk import TweetTokenizer
import re

class Placeholder():

    def __init__(self,filepath):
        self._filepath= filepath
        self._counts = 0
        self._totalcount = 0

    def write_tweet_txt_file(self):
        with codecs.open(self._filepath+".json","r","latin-1") as f:
            tweets = json.load(f,encoding = "utf-8")
            with open(self._filepath+".txt","w") as file:
                for i in range(len(tweets)):
                    file.write(tweets[i]["text"]+"\n")

    def ngrams(self):
#        name = re.findall("\w+$",self._filepath)
        name = str(input("choose a seed: "))
        with codecs.open(self._filepath+".txt","r","latin-1") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
        emptylist=[]
        maxhistory = int(input("Choose n for ngram, preferably 2 or 3: "))
        for i in range(2, maxhistory+1):
            emptylist+=nltk.ngrams(tknz_lines, i)
        cfd=ConditionalFreqDist([(tuple(a), b) for *a,b in emptylist])
        seed=[name]
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

    def text_most_common(self):
        with codecs.open(self._filepath+".txt","r","latin-1") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
            n = int(input("Choose an N for the amount of most common: "))
            self._mostcommon = Counter(tknz_lines).most_common(n)
        return self._mostcommon

    def text_total_counts(self):
        with codecs.open(self._filepath+".txt","r","latin-1") as f:
            lines = f.read()
            tknzr = TweetTokenizer()
            tknz_lines =tknzr.tokenize(lines)
            self._totalcount = len(tknz_lines)
        return self._totalcount

    def hashtag_tracker(self):
        hashlist=[]
        txt=codecs.open(self._filepath+".txt","r","latin-1")
        reader=txt.read()
        for line in reader:
            hashtags=re.findall(r"#(\w+)", line)
            for hashtag in hashtags:
                if hashtag != "":
                    hashlist.append(hashtag)

        count=Counter(hashlist)
        txt.close()
        return count.most_common(100)


    def link_and_hashtag_remover(self):
        text_file = open(self._filepath+"-notrash.txt", "w")
        with codecs.open(self._filepath+".txt","r","latin-1") as f:
            lines=f.read()
            nolinks = re.sub("htt.+:[\/||\w||.||\-||=]+", "link_placeholder", lines)
            hashless=re.sub(r"#(\w+)", '', nolinks, flags=re.MULTILINE)
            s = re.sub("[\/||\w||.||\-]+.dk", '',hashless)
            text_file.write(s)
            text_file.write("\n")
            
