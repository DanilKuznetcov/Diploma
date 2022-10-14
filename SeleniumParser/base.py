from abc import ABC, abstractstaticmethod
from typing import Dict, Union

from selenium.webdriver.common.by import By

class BaseItem(ABC):
    '''Базовый класс предмета, который мы ищем'''

    container_tag: str # Это тег контейнер на странице, котороый содержит искомые элементы
    item_tag: str # Это тег самого искомого элемента на странице

    @abstractstaticmethod
    def __init__(*args, **kwargs) -> Union[str, Dict[str, str], None]:
        '''Функция для обработки тега html в то, что нужно получить от данного элемента'''


class CommentItem(BaseItem):
    '''Класс комментария'''
    # container_tag = 'wl_replies_block_wrap'
    # item_tag = 'reply'
    container_tag = 'replies_list'
    item_tag = 'reply'

    def __init__(self, comment, *args, **kwargs):
        '''Парсит коментарий. На вход принимает элемент с классам reply
        '''

        self.comment_id = comment.get_attribute('data-post-id')
        # x = comment.get_attribute('onclick')
        # reply_post_id = 'post' + comment.get_attribute('onclick').split("'")[1]
        # time = comment.find_element(By.CLASS_NAME, 'rel_date').text

        text = comment.text
        #Тригер есть не всегда
        is_reply1 = comment.find_elements(By.CLASS_NAME, 'mem_link') != []
        is_reply2 = comment.find_elements(By.CLASS_NAME, 'wall_reply_greeting') != []
        is_reply_on_reply = comment.find_elements(By.CLASS_NAME, 'reply_to') != []

        if is_reply_on_reply:
            self.trigger_type = 'R'
            self.trigger_id = comment.find_element(By.CLASS_NAME, 'reply_to').get_attribute('data-root-id')
        elif is_reply1 or is_reply2:
            self.trigger_type = 'C'
            self.trigger_id = comment.find_element(By.XPATH, '..').get_attribute('id')[7:]
            # self.trigger_id = comment.find_elements(By.CLASS_NAME, 'mem_link')[0].parent
            # self.trigger_id = comment.find_elements(By.CLASS_NAME, 'wall_reply_greeting')[0].get_attribute('onclick').split(',')
            # x = 7
        else:
            self.trigger_type = 'P'
            self.trigger_id = comment.find_element(By.XPATH, '..').get_attribute('id')[7:]

        # except:
        #     pass
            # self.replied_to_id = None

        try:
            self.author = comment.find_element(By.CLASS_NAME, 'author').get_attribute('href')
            self.text = comment.find_element(By.CLASS_NAME, 'reply_text').text
            self.like_count = comment.find_element(By.CLASS_NAME, 'like_cont').text
            self.date = comment.find_element(By.CLASS_NAME, 'rel_date').text
        except:
            self.author = None
            self.text = None
            self.like_count = None
            self.date = None

        if self.like_count == '':
            self.like_count



    def __repr__(self) -> str:
        return f'\n<Comment: comment_id={self.comment_id}, trigger_type={self.trigger_type}, trigger_id={self.trigger_id}, author={self.author}, like_count={self.like_count}, date={self.date}, text={self.text}>'
