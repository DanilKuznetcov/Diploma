import GetPostsVKAPI
import SeleniumParser.GetCommentsSelenium
from datetime import datetime, timedelta
import dbConnecter


if __name__ == '__main__':
    data = []
    start = datetime(2022, 8, 11, 13)
    end = datetime(2022, 8, 11, 13, 30)
    delta = timedelta(hours=1)

    all_data = GetPostsVKAPI.get_posts('COVID-19', start, end, delta)
    # GetCommentsVKAPI.tranform_to_excel(filtered)

    db = dbConnecter.db_adapter()
    for post in all_data:
        db.insert_post(post)
        # db.insert_comments(post)
        comments = SeleniumParser.GetCommentsSelenium.get_comment(post)
        print(comments)
    db.close_adapt()

    # push_comments_to_csv('2021-06-11-12.csv')
