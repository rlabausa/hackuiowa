from afinn import Afinn
from nytimesarticle import articleAPI
from matplotlib import pyplot as plt 
import time

api = articleAPI('f20dfc17dd8745aab3d1342093519e42') # change to use your own nyt API Key
afinn = Afinn()

#count = 0
headline_score = 0.0

positive = 0
negative = 0
neutral = 0

for i in range(0, 1):
    articles = api.search(
        q='Clinton, Bill', begin_date=19980101, end_date=19980201, page=i)
    for a in articles['response']['docs']:
        current_score = float(afinn.score(a['headline']['main']))
        if(current_score > 0):
            positive += 1
        elif(current_score < 0):
            negative +=1
        else:
            neutral +=1
        
        
        headline_score += current_score
        #count += 1
        
        time.sleep(.5) #nyt limits 5 requests per second
    
print("overall headline score: ", headline_score)      
print("positive: ", positive)
print("negative: ", negative)
print("neutral: ", neutral)

labels = 'Positive', 'Negative', 'Neutral'
total = (positive + negative + neutral) 
sizes = [positive/total, negative/total, neutral/total]
explode = (0, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels =labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
plt.show()



