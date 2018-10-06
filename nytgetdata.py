from nytimesarticle import articleAPI
api = articleAPI('API-Key')

articles = api.search(q='Clinton', begin_date=19990101,
                      end_date=19990401)

# Abstract
print(articles['response']['docs'][0]['abstract'])

# Headline
print(articles['response']['docs'][0]['headline']['main'])

# Publication Date
print(articles['response']['docs'][0]['pub_date'])
