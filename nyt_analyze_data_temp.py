from nytimesarticle import articleAPI
import time
api = articleAPI('*API Key*')

# articles = api.search(q='Clinton, Bill', begin_date=19980101,
#                      end_date = 19980201, page=1)

# print(articles)
count = 0
for i in range(0, 5):
    articles = api.search(
        q='Clinton, Bill', begin_date=19980101, end_date=19980201, page=i)
    for a in articles['response']['docs']:
        print(a['abstract'])
        print(a['headline']['main'])
        print(a['pub_date'])
        print('****************')
        count += 1
        time.sleep(.5)
print(count)
