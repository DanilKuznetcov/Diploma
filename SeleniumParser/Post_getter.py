import csv

class PostReader:
    '''Класс для работы с CSV'''
    def __init__(self, path, chrome=False, web_driver=None) -> None:
        self.path = path

    def create_csv_reader(self):
        with open(self.path) as csvfile:
            for row in csv.reader(csvfile):
                if row[1] == 'date':
                    continue
                yield row
