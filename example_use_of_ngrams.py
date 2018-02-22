# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:46:17 2018

@author: jeppe
"""
from placeholdername import placeholder
import re
path1= "twitterdata/amager"
path2= "instagram/scrapefiles/amager"
ph1 = placeholder(path1)
print(ph1.Ngrams())

ph2 = placeholder(path2)
print(ph2.Ngrams())

