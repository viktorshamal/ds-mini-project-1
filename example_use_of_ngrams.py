# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:46:17 2018

@author: jeppe
"""
from placeholdername import Placeholder

path1= "twitterdata/vesterbro"
path2= "instagram/scrapefiles/vesterbro"

ph1 = Placeholder(path1)
ph1.link_and_hashtag_remover()

ph2 = Placeholder(path2)
ph2.link_and_hashtag_remover()