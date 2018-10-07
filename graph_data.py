import create_graphs
import mysql.connector


mydb = mysql.connector.connect(
    host="sql169.main-hosting.eu",
    user="u728211364_lily",
    passwd="helloworld1",
    database="u728211364_ravio"
)

news_src = ['Wall Street Journal', 'CNN', 'Fox News',
            'MSNBC', 'CBS News', 'The New York Times']
positive_nums = [0] * 6
negative_nums = [0] * 6
neutral_nums = [0] * 6

week1_nums = [0] * 6
week2_nums = [0] * 6
week3_nums = [0] * 6
week4_nums = [0] * 6

# for every item in that list, 3 queries: +, -, 0; add to index i in those 3 lists


for i in range(0, 6):
    mycursor = mydb.cursor(buffered=True)

    source_id = i + 2

    mycursor.execute(
        "SELECT num_positive_score FROM source WHERE source_id= %s", [source_id])
    positive_score = mycursor.fetchone()[0]
    # print(positive_score)

    positive_nums.insert(i, positive_score)

    mycursor.execute(
        "SELECT num_negative_score FROM source WHERE source_id= %s", [source_id])
    negative_score = mycursor.fetchone()[0]
    # print(negative_score)

    negative_nums.insert(i, negative_score)

    mycursor.execute(
        "SELECT num_neutral_score FROM source WHERE source_id= %s", [source_id])
    neutral_score = mycursor.fetchone()[0]
    # print(neutral_score)

    neutral_nums.insert(i, neutral_score)

    ####

    mycursor.execute(
        "SELECT SUM(score) FROM article WHERE pub_date >= '20180906' and pub_date < '20180913' and source_id= %s", [source_id])
    week1_sum = mycursor.fetchone()[0]
    # print(week1_sum)
    week1_nums.insert(i, week1_sum)

    mycursor.execute(
        "SELECT SUM(score) FROM article WHERE pub_date >= '20180913' and pub_date < '20180920' and source_id= %s", [source_id])
    week2_sum = mycursor.fetchone()[0]
    # print(week2_sum)
    week2_nums.insert(i, week2_sum)

    mycursor.execute(
        "SELECT SUM(score) FROM article WHERE pub_date >= '20180920' and pub_date < '20180927' and source_id= %s", [source_id])
    week3_sum = mycursor.fetchone()[0]
    # print(week3_sum)
    week3_nums.insert(i, week3_sum)

    mycursor.execute(
        "SELECT SUM(score) FROM article WHERE pub_date >= '20180927' and pub_date < '20181007' and source_id= %s", [source_id])
    week4_sum = mycursor.fetchone()[0]
    # print(week4_sum)
    week4_nums.insert(i, week4_sum)

create_graphs.basic_bar(news_src, positive_nums, negative_nums, neutral_nums)
create_graphs.stacked_bar(news_src, positive_nums, negative_nums, neutral_nums)
create_graphs.line_graph(news_src, week1_nums,
                         week2_nums, week3_nums, week4_nums)
