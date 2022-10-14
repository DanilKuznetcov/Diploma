import SeleniumParser.Post_getter
import SeleniumParser.driver


def get_comment(post):
    brows_manage = SeleniumParser.driver.CustomBrowserManager()
    url = f'https://vk.com/wall{post["owner_id"]}_{post["id"]}'
    count = int(post['comments']['count'])
    return brows_manage.comments(url, count)

