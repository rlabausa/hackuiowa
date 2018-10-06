from afinn import Afinn
from nytimesarticle import articleAPI

afinn = Afinn()
api = articleAPI('f20dfc17dd8745aab3d1342093519e42')

articles = api.search(q='Clinton', begin_date=19990101,
                      end_date=19990401)

abstract = articles['response']['docs'][0]['abstract']
headline = articles['response']['docs'][0]['headline']['main']
pub_date = articles['response']['docs'][0]['pub_date']

print("abstract: ", afinn.score(abstract), " headline: ", afinn.score(headline), " publication date: ", afinn.score(pub_date))

print(float(afinn.score(abstract)) + float(afinn.score(headline)) + float(afinn.score(pub_date)))




