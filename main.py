import json
import re
import hashlib


class Wikipedia:

    URL = 'https://en.wikipedia.org/wiki/'

    def __init__(self, path_: str):
        self.countries = read_json(path_)

    def __iter__(self):
        return self

    def __next__(self):
        if self.countries:
            country = self.countries.pop(0)['name']['common']
            return country + ' - ' + self.URL + re.sub(r'\s+', '_', country)
        else:
            raise StopIteration


def read_file_md5_line(path_: str):
    with open(path_, encoding='utf-8') as f:
        for line in f:
            yield hashlib.md5(line.encode()).hexdigest()


def write_file(file_info, path_: str):
    with open(path_, 'w', encoding='utf-8', ) as f:
        return f.write(file_info)


def read_json(path_: str):
    with open(path_, encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    print('Задача 1.\n')
    path = 'countries.json'
    country_information = []
    for country_link in Wikipedia(path):
        print(country_link)
        country_information += [country_link]
    path_2 = 'country_information.txt'
    write_file('\n'.join(country_information), path_2)
    print('-'*30, '\n'*2)
    print('Задача 2.\n')
    for line_md5 in read_file_md5_line(path_2):
        print(line_md5)
