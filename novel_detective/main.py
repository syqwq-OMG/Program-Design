# coding = utf-8
# author = syqwq

from NDetective import *

PATH = r'./novel.txt'


if __name__ == '__main__':
    nvd = NDetective(Novel(PATH), 20, parse_relation_strategy=CHAPTER_AS_A_WHOLE)
    nv = nvd.novel

    print('=' * 10 + 'all titles' + '=' * 10)
    for title, chapter in zip(nv.get_all_titles(), nv.get_all_chapters()):
        print(f'{title:<30} \t#words: {len(chapter)}')

    print('=' * 10 + 'main characters' + '=' * 10)
    characters_freq = nvd.get_chatacter_freq()
    for ch, freq in characters_freq.items():
        first_appear = nv.which_chapter(nv.source.index(ch))
        print(f'Character: {ch:<10}\tFrequency: {freq}\tFirst appear in Chapter: {first_appear}')

    print('=' * 10 + 'TOP 10 closest relationship' + '=' * 10)
    it = iter(nvd.relationships.items())
    for i in range(1, 11):
        (ch1, ch2), cnt = next(it)
        print(f'TOP {i}:\t {ch1}<-->{ch2} \t interacts {cnt} times')

    print('=' * 10 + 'WIN or LOSE' + '=' * 10)
    battles = nvd.battles
    for ch in battles.keys():
        print(f'{ch:<5}\t WIN: {battles[ch]['wins']:<7}\t LOSE: {battles[ch]['losses']}')
