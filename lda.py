from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation
import glob
import os
import codecs

path = 'D:\Documents\GitHub\Project 1\\twitterdata\\nørrebro.txt'
        
documents = open(path,encoding="utf8")

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" %(topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

def getiterator():
	for line in documents:
		for word in line.split():
			yield word

def filetolda():
	documents = open(path,encoding="utf8")

	no_features = 1000
	no_topics = 10
	no_top_words = 10

	# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
	tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features,stop_words=None)
	tf = tf_vectorizer.fit_transform(getiterator())
	tf_feature_names = tf_vectorizer.get_feature_names()

	# Run LDA
	lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)
	display_topics(lda, tf_feature_names, no_top_words)

def filetonmf():
	documents = open(path,encoding="utf8")

	no_features = 1000
	no_topics = 10
	no_top_words = 10

	
	tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words= None)
	tfidf = tfidf_vectorizer.fit_transform(getiterator())
	tfidf_feature_names = tfidf_vectorizer.get_feature_names()

	# Run NMF
	nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)
	display_topics(nmf, tfidf_feature_names, no_top_words)
	
filetonmf()
