import SeleniumParser.Post_getter
import SeleniumParser.driver


def push_comments_to_csv(csv_name):
    brows_manage = SeleniumParser.driver.CustomBrowserManager()
    reader_manager = SeleniumParser.Post_getter.PostReader(csv_name)
    reader = reader_manager.create_csv_reader()
    c = 1
    for post in reader:
        url = f'https://vk.com/wall{post[3]}_{post[2]}'
        count = int(post[6])
        comments = brows_manage.comments(url, count)
        for comment in comments:
            print(f'{c}: ', comment)
        c += 1
