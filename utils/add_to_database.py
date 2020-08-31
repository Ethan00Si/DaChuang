import mysql.connector
import pandas as pd


# 向article里面插入新闻
def insert_to_article(cursor, db, news_list):

    for item in news_list:
        file_path, art_type = item
        data_csv = pd.read_csv(file_path)
        print('current_file: ', file_path)
        for index, row in data_csv.iterrows():
            print(index, end='\r')
            source = str(row['source'])
            url = str(row['url'])
            title = str(row['title'])
            content = str(row['content'])
            if content == 'nan':
                content = ''
            time = row['datetime'].replace('-', '')+'000000'

            values = (source, url, title, content, art_type, time)
            sql = 'INSERT INTO article (art_source, art_url, art_title, art_content, art_type, art_time) VALUES (%s, %s, %s, %s, %s, %s)'
            # try:
            cursor.execute(sql,  values)
            db.commit()
            # except:
            #     print(values)
            #     exit(0)


def add_news(file_list):
    """
    把新闻添加到table “article”中
    """
    db = mysql.connector.connect(host='localhost',
                                 port=3306,
                                 user='root',      # 数据库IP、用户名和密码
                                 passwd='123456',
                                 charset='utf8',
                                 database='Dachuang'  # 数据库的名字 需要先创建才能连接
                                 )

    # db = mysql.connector.connect(
    #         host='183.174.228.33',
    #         port = 8282,
    #         user='root',
    #         passwd='123456',
    #         database ='ructoutiao',
    #         charset='utf8'
    # 使用 cursor() 方法创建一个游标对象 cursor
    # )
    cursor = db.cursor()

    cursor.execute("SET NAMES utf8mb4")  # 使用utf8mb4 部分汉字以及所有emoji都是这个
    cursor.execute("SET CHARACTER SET utf8mb4")
    cursor.execute("SET character_set_connection = utf8mb4")

    insert_to_article(cursor, db, file_list)