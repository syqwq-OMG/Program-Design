# coding = utf-8
# author = syqwq

from NDetective import *

PATH = r'./novel.txt'
STOPWORDS_PATH = r'./stopwords.txt'


def save_data(data, path=None):
    if path is None:
        path = './{}.txt'.format(data)
    with open(path, 'w', encoding='utf-8') as f:
        try:
            for i in data:
                f.write(i + '\n')
        except TypeError:
            f.write(data)


if __name__ == '__main__':
    nv = Novel(PATH)
    nvd = NDetective(nv)
    print('=' * 10 + 'all titles' + '=' * 10)
    for title, chapter in zip(nv.get_all_titles(), nv.get_all_chapters()):
        print(f'{title:<30} \t#words: {len(chapter)}')

    print('=' * 10 + 'all titles' + '=' * 10)

    print(nvd.characters.index[:20])
