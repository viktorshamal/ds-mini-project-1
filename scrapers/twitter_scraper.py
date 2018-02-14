# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 14:23:25 2018

@author: jeppe
"""

import requests
import json


headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'}
params = {
    "q": "nørrebro",
    "count": 100
}

response = requests.get(
        "https://api.twitter.com/1.1/search/tweets.json",
        params=params,
        headers=headers)

tweets = json.loads(response.text)["statuses"]

for tweet in tweets:
    print(tweet["text"])
    
print(len(tweets))