from newsapi import NewsApiClient
import time

newsapi = NewsApiClient(api_key='*API Key*')

count = 0
for i in range(1, 50):
    top_headlines = newsapi.get_everything(q='Kavanaugh&',
                                           sources='fox-news',
                                           language='en', page=i)
    for a in top_headlines['articles']:
        print(a['title'])
        print(a['description'])
        print(a['publishedAt'])
        print('****************')
        count += 1
        time.sleep(.5)
print(count)
