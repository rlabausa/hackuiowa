from afinn import Afinn
from nytimesarticle import articleAPI
from matplotlib import pyplot as plt 
import time
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.plotting import figure

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

news_sources = ['New York Times','Fox News', 'BBC']
sentiment_bias = ['Positive', 'Negative', 'Neutral']
colors = ["#c9d9d3", "#718dbf", "#e84d60"]

data = {'news_sources' : news_sources,
        'Positive'   : [positive, positive, positive],
        'Negative'   : [negative, negative, negative],
        'Neutral'   : [neutral, neutral, neutral]}

p = figure(x_range=news_sources, plot_height=300, title="Sentiment by News Source",
           toolbar_location=None, tools="hover", tooltips="$name @news_sources: @$name")

p.vbar_stack(sentiment_bias, x='news_sources', width=0.9, color=colors, source=data,
             legend=[value(x) for x in sentiment_bias])

p.y_range.start = 0
p.y_range.range_padding = 2.0 # math.max(*the 6 possible sources*) + padding
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_right"
p.legend.orientation = "horizontal"
show(p)




