#from yelp.client import Client
#from yelp.oauth1_authenticator import Oauth1Authenticator
import yelp

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)
params = {
    'term': 'food',
    'lang': 'fr'
}

client = Client(auth)

#search by search
client.search('San Francisco', **params) 

#search by boundingbox
client.search_by_bounding_box(
    37.900000,
    -122.500000,
    37.788022,
    -122.399797,
    **params
)