import requests
from datetime import datetime, timedelta
import time
import pandas as pd
from constants import *


def search_posts(theme, start, final):
    delta = timedelta(hours=1)

    api_method = f'{API_URL}/newsfeed.search'
    data = []
    data_temp = []

    while start < final:
        end = start + delta
        start_from = ''
        f = True
        while f:
            params = {
                'access_token': ACCESS_TOKEN,
                'count': 200,
                'start_time': time.mktime(start.timetuple()),
                'end_time': time.mktime(end.timetuple()),
                'q': theme,
                'v': V
            }
            if start_from != '':
                params['start_from'] = start_from
            resp = requests.get(api_method, params)
            data += resp.json()['response']['items']
            f = 'next_from' in resp.json()['response']
            if f:
                start_from = resp.json()['response']['next_from']
        start = end
        data_temp.append(len(data))
    return data


# def filter_data(data):
#     data = list(filter(lambda x: x['post_type'] == 'post' and x['comments'] != '0', data))
#     for d in data:
#         if 'attachments' in d: del d['attachments']
#         del d['post_type']
#         d['date'] = datetime.fromtimestamp(d['date'])
#         if 'marked_as_ads' in d: del d['marked_as_ads']
#         if 'views' in d: d['views'] = d['views']['count']
#         if 'likes' in d: d['likes'] = d['likes']['count']
#         if 'reposts' in d: d['reposts'] = d['reposts']['count']
#         if 'comments' in d: d['comments'] = d['comments']['count']
#     return data


# def tranform_to_excel(data):
#     df = pd.DataFrame(data, columns=['date', 'id', 'owner_id', 'from_id', 'text', 'comments', 'likes', 'reposts', 'views'])
#     df = df[df['comments'] > 0]
#     df.to_csv('SeleniumParser/2021-06-11-12.csv')


def get_posts(topic, start, end, delta):
    all_data = search_posts('COVID-19', start, end)
    return all_data
