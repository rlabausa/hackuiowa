import pygal 

def basic_bar(news_src, num_pos, num_neg, num_neut):
    bar_chart = pygal.Bar()
    bar_chart.title = 'Sentiment Across News Sources'
    bar_chart.x_labels = [news_src[0], news_src[1], news_src[2], news_src[3], news_src[4], news_src[5]]
    bar_chart.add('Positive',[num_pos[0], num_pos[1], num_pos[2], num_pos[3], num_pos[4], num_pos[5]])
    bar_chart.add('Negative',  [num_neg[0], num_neg[1], num_neg[2], num_neg[3], num_neg[4], num_neg[5]])
    bar_chart.add('Neutral',     [num_neut[0], num_neut[1], num_neut[2], num_neut[3], num_neut[4], num_neut[5]])
    bar_chart.render_to_file('basic_bar.svg')   

def stacked_bar(news_src, num_pos, num_neg, num_neut):
    bar_chart = pygal.StackedBar()
    bar_chart.title = 'Sentiment Across News Sources'
    bar_chart.x_labels = [news_src[0], news_src[1], news_src[2], news_src[3], news_src[4], news_src[5]]
    bar_chart.add('Positive',[num_pos[0], num_pos[1], num_pos[2], num_pos[3], num_pos[4], num_pos[5]])
    bar_chart.add('Negative',  [num_neg[0], num_neg[1], num_neg[2], num_neg[3], num_neg[4], num_neg[5]])
    bar_chart.add('Neutral',     [num_neut[0], num_neut[1], num_neut[2], num_neut[3], num_neut[4], num_neut[5]])
    bar_chart.render_to_file('stacked_bar.svg')   


# src = ['NYT', 'WSJ', 'FOX', 'CNN', 'CBS', 'BBC']
# pos = [1,2,3,4,5,6,7]
# neg= [1,2,3,4,5,6,7]
# neut= [1,2,3,4,5,6,7]
# basic_bar(src, pos, neg, neut)

