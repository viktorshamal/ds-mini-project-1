import requests
import json
import pprint
import glob
import os
import re

pp = pprint.PrettyPrinter()


def article_file_to_ids():
    path = '../infomedia_data/'
    article_files = glob.glob(path + "*.json")

    for af in article_files:
        path = os.path.splitext(af)[0]
        articles = json.load(open(af, errors="replace"))['Articles']

        with open(path + '_ids_.txt', 'w') as f:
            for article in articles:
                f.write(article['Duid'] + '\n')


def get_article(id):
    url = "https://apps.infomedia.dk/mediearkiv/article/getarticlebodytext"

    payload = "{\r\n   \"ArticleId\":\"" + id + \
        "\",\r\n   \"BasicSearchFilter\":{\r\n      \"SearchClause\":{\r\n         \"AvailableSearchLocations\":[\r\n            0,\r\n            1,\r\n            2,\r\n            3\r\n         ]\r\n      }\r\n  }\r\n}"
    headers = {
        'Host': "apps.infomedia.dk",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
        'Cookie': "Insight.Web.Ms.SessionId=nmn3duoyxcejsvgvj0iq4hef",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache",
        'Postman-Token': "6d23f872-bf1b-0247-912b-cc9ac2078068"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    data = json.loads(response.text)

    return data


def scrape_articles(district):
    path = '../infomedia_data/'
    filename = path + district + '_ids_.txt'
    writefile = open(path + district + '.txt', 'w', errors="replace")

    with open(filename) as f:
        for ids in f:
            article = get_article(ids)
            text = article['BodyText'] + '\n' + article['Subheading'] + '\n'
            text = re.sub('<[^<]+?>', '', text)
            writefile.write(text)


for district in ['vesterbro', 'amager', 'østerbro', 'indreby', 'nørrebro']:
    print('Start scraping: ' + district)
    scrape_articles(district)
