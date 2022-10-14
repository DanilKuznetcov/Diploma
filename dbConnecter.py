import mysql.connector
import constants
from constants import *


class db_adapter:

    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="danil",
            password="24092022"
        )

        self.mycursor = self.db.cursor()
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS diplom")
        self.mycursor.execute("USE diplom")

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Posts (
            ID VARCHAR(20) PRIMARY KEY,
            date DATETIME,
            text VARCHAR(4000),
            count_comments INT,
            count_likes INT,
            count_reporsts INT,
            count_views INT
        )""")

        self.db.commit()

    def insert_post(self, post):
        insert = "INSERT IGNORE INTO Posts VALUES (%s, FROM_UNIXTIME(%s), %s, %s, %s, %s, %s)"

        values = [f"{post['owner_id']}_{post['id']}", post['date'], post['text'],
                  post['comments']['count'], post['likes']['count'],
                  post['reposts']['count'],
                  post['views']['count'] if 'views' in post else None]

        self.mycursor.execute(insert, values)

    def insert_comments(self, post):
        insert = "INSERT IGNORE INTO Posts VALUES (%s, FROM_UNIXTIME(%s), %s, %s, %s, %s, %s)"

    def close_adapt(self):
        self.db.commit()
        self.db.close()
