from unittest import TestCase
import SeleniumParser.GetCommentsSelenium
import requests
from constants import *
import warnings

class Test(TestCase):
    def setUp(self):
        """... code to execute in preparation for tests ..."""
        warnings.simplefilter("ignore")
        api_method = f'{API_URL}/wall.getById'
        resp = requests.get(api_method, params={
            'access_token': ACCESS_TOKEN,
            'posts': f'-71631912_6255155',
            'v': V
        })
        self.post = resp.json()['response'][0]
        self.comments = list(SeleniumParser.GetCommentsSelenium.get_comment(self.post))

    def test_get_comment(self):
        result = SeleniumParser.GetCommentsSelenium.get_comment(self.post)
        print(list(result))

    def test_correct_trigger(self):
        self.assertIsNotNone(self.comments[1])
