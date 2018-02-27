from InstagramAPI import InstagramAPI
import time


# stop conditions, the script will end when first of them will be true
def hashsearch(hashtag, max_pages):
    next_max_id = ''
    for i in range(int(max_pages)):
        API.getHashtagFeed(hashtag, next_max_id)
        Jayson= API.LastJson
        for post in Jayson["items"]:
            try:
                txt.write(post["caption"]["text"]+"\n\n")
            except:
                pass
        time.sleep(2)
        try:
            next_max_id = Jayson["next_max_id"]
        except Exception:
             print("No 'next_max_id' value found")

API = InstagramAPI("KongKarlAfKarlebo", "Kavery97")
API.login()

hashtag=input("What hashtag do you wish to scrape from? (No capital letters): ")
max=input("How many requests do you wish to send? 1 Request returns 7 instagram posts: ")
txt = open(hashtag+".txt", "w")
hashsearch(hashtag, max)
txt.close()
