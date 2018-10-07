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
    totals = [num_pos[0] + num_neg[0] + num_neut[0], num_pos[1] + num_neg[1] + num_neut[1], num_pos[2] + num_neg[2] + num_neut[2], num_neut[3]+ num_pos[3] + num_neg[3],
                num_pos[4] + num_neg[4] + num_neut[4], num_pos[5] + num_neg[5] + num_neut[5]]
    bar_chart = pygal.StackedBar()
    bar_chart.title = 'Sentiment Across News Sources'
    bar_chart.x_labels = [news_src[0], news_src[1], news_src[2], news_src[3], news_src[4], news_src[5]]
    bar_chart.add('Positive',[(num_pos[0]/ totals[0]) , (num_pos[1]/ totals[1]), (num_pos[2]/ totals[2]), (num_pos[3]/totals[3]), (num_pos[4]/totals[4]), (num_pos[5]/totals[5])])
    bar_chart.add('Negative',  [(num_neg[0]/ totals[0]), (num_neg[1]/ totals[1]), (num_neg[2]/ totals[2]), (num_neg[3]/ totals[3]), (num_neg[4]/ totals[4]), (num_neg[5]/ totals[5])])
    bar_chart.add('Neutral', [(num_neut[0]/totals[0]), (num_neut[1]/totals[1]), (num_neut[2]/totals[2]), (num_neut[3]/totals[3]), (num_neut[4]/totals[4]), (num_neut[5]/totals[5])])
    bar_chart.render_to_file('stacked_bar.svg')   


def line_graph(news_src, week1_nums, week2_nums, week3_nums, week4_nums):
    line_chart = pygal.Line()
    line_chart.title = 'Sentiment Analysis Score Over 4 Weeks'
    line_chart.x_labels = map(str, range(1, 4))
    line_chart.add(news_src[0], [week1_nums[0],
                                 week2_nums[0], week3_nums[0], week4_nums[0]])
    line_chart.add(news_src[1], [week1_nums[1],
                                 week2_nums[1], week3_nums[1], week4_nums[1]])
    line_chart.add(news_src[2], [week1_nums[2],
                                 week2_nums[2], week3_nums[2], week4_nums[2]])
    line_chart.add(news_src[3], [week1_nums[3],
                                 week2_nums[3], week3_nums[3], week4_nums[3]])
    line_chart.add(news_src[4], [week1_nums[4],
                                 week2_nums[4], week3_nums[4], week4_nums[4]])
    line_chart.add(news_src[5], [week1_nums[5],
                                 week2_nums[5], week3_nums[5], week4_nums[5]])

    line_chart.render_to_file('line_graph.svg')

