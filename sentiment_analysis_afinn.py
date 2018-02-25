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

def sentimentscore():
    af = afinn.Afinn(language="da")
    path = '../infomedia_data/'
    text_files = glob.glob(path + "*.txt")
    results = []
    for tf in text_files:
        path = os.path.splitext(tf)[0]
        with codecs.open(tf,encoding = "latin-1" )['Articles'] as f:
            text = f.read()
            score = af.score(text)
            results.append(score)
#        with codecs.open(articles,encoding = "latin-1") as f:
    return results

print(sentimentscore())
