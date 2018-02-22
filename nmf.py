from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import NMF, LatentDirichletAllocation
import glob
import os
import codecs

path = 'D:\Documents\GitHub\Project 1\\twitterdata\\nørrebro.txt'
        
#documents = ''

def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d:" %(topic_idx))
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]]))

def getiterator():
	for line in documents:
		for word in line.split():
			yield word

documents = open(path,encoding="utf8")

	#for line in documents:
		#print(line)

	
#for filename in glob.glob(os.path.join(path, '*.txt')):
    #documents = open(filename,'r')

no_features = 1000


# LDA can only use raw term counts for LDA because it is a probabilistic graphical model
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features,stop_words=None)
tf = tf_vectorizer.fit_transform(getiterator())
tf_feature_names = tf_vectorizer.get_feature_names()


no_topics = 10

# Run LDA
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)

no_top_words = 10
display_topics(lda, tf_feature_names, no_top_words)	