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

ph = placeholder("amager")
print(ph.Bigrams("amager"))
print(ph.Trigrams("amager"))
#                