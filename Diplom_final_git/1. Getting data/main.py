import GetCommentsVKAPI
from GetCommentsVKAPI import tranform_to_excel
from datetime import datetime, timedelta


if __name__ == '__main__':
    data = []
    start = datetime(2022, 1, 1)
    end = datetime(2022, 1, 2)
    delta = timedelta(hours=3)


    topic = "крипта"
    filtered = GetCommentsVKAPI.get_posts(topic, start, end, delta)
    GetCommentsVKAPI.tranform_to_excel(filtered, topic, f'{start}-{end}')
