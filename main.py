import GetCommentsVKAPI
from SeleniumParser.GetCommentsSelenium import push_comments_to_csv
from datetime import datetime, timedelta


if __name__ == '__main__':
    # data = []
    # start = datetime(2022, 8, 11, 13)
    # end = datetime(2022, 8, 11, 13, 30)
    # delta = timedelta(hours=1)
    #
    # filtered = GetCommentsVKAPI.get_posts('COVID-19', start, end, delta)
    # GetCommentsVKAPI.tranform_to_excel(filtered)

    push_comments_to_csv('2021-06-11-12.csv')
