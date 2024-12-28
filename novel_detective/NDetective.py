import jieba.posseg as pseg
import pandas as pd
from Novel import *
from collections import defaultdict, OrderedDict
import re

EXCLUDE_NAMES = ['魏兵', '却说', '将军', '二人', '荆州', '商议', '军士', '军马', '引兵', '次日', '大喜', '曹兵']
CHAPTER_AS_A_WHOLE = lambda x: x
SPLIT_LINES = lambda x: x.split('\n')

WIN_KEYWORDS = ['胜', '大胜', '胜利', '战胜', '取胜', '成功', '克敌制胜', '击败', '夺取', '打败']
LOSE_KEYWORDS = ['败', '败北', '失败', '落败', '溃败', '败阵', '败退', '失败', '败逃']


def iterate(obj):
    """
    expand a n-dim list to a plain list
    :param obj: a n-dim list
    :return: a plain list
    """
    if not isinstance(obj, list):
        return [obj]

    ret = []
    for x in obj:
        ret += iterate(x)
    return ret


class NDetective:
    @staticmethod
    def merge_name(name: str) -> str | None:
        """
        give the representative name of a character which makes counts of a chracter more precise
        :param name: a name of a character
        :return: the representive name of a character
        """
        if name in EXCLUDE_NAMES:
            return None
        elif name in (d := ['诸葛亮', '孔明', '孔明曰', '丞相']):
            return d[0]
        elif name in (d := ['刘备', '玄德', '玄德曰']):
            return d[0]
        else:
            return name

    @staticmethod
    def count_occurance_in_context(per1: str, per2: str, context: str) -> int:
        """
        count the number of common occurences of two character in a context
        :param per1: character 1
        :param per2: character 2
        :param context: a given paragraph
        :return: the count of common occurences of two character in a context
        """
        return min(context.count(per1), context.count(per2))

    def __init__(self, novel: Novel,
                 character_num: int = 20,
                 parse_relation_strategy=CHAPTER_AS_A_WHOLE):
        """
        :param novel: a Novel object
        :param character_num: the main chatacter number expected
        :param parse_relation_strategy: strategy to get a context
        """
        self.novel = novel
        self.strategy = parse_relation_strategy
        self.character_num = character_num

        self.characters = self.parse_name_freq()

        self.relationships = defaultdict(int)
        self.parse_relations()

        self.battles = dict()
        self.parse_battles()

    def parse_name_freq(self) -> pd.Series:
        """
        parse all the names and occurances count of each character
        :return: a pandas Series object with the names and occurances count
        """
        names = []
        for word, flag in pseg.cut(self.novel.source, use_paddle=True):
            if flag != 'nr':
                continue
            word = NDetective.merge_name(word)
            if word is not None and len(word) > 1:
                names.append(word)
        return pd.Series(names).value_counts()

    def get_chatacter_freq(self) -> dict[str, int]:
        """
        get a dict of character name and occurances count of first character num
        :return: an ordered dict of character name and occurances count
        """
        return dict(self.characters[:self.character_num])

    def parse_relations(self):
        chars = list(self.get_chatacter_freq().keys())[:self.character_num]

        for chp_num in range(1, self.novel.titles_num + 1):
            chp = self.novel.get_content_of_chapter(chp_num)

            chp = self.strategy(chp)
            for context in iterate(chp):
                for idx, char1 in enumerate(chars):
                    for char2 in chars[idx + 1:]:
                        self.relationships[(char1, char2)] += (
                            NDetective.count_occurance_in_context(char1, char2, context))

        self.relationships = OrderedDict(
            sorted(self.relationships.items(),
                   key=lambda x: x[1],
                   reverse=True))

    def parse_battles(self):
        """
        parse all the wins and losses of each character
        :return get all the wins and losses of each character
        """

        battles = {char: {'wins': 0, 'losses': 0} for char in self.get_chatacter_freq().keys()}

        for char in self.get_chatacter_freq().keys():
            for win_keyword in WIN_KEYWORDS:
                wins = len(re.findall(f'{char}.*?{win_keyword}', self.novel.source))
                battles[char]['wins'] += wins

            for lose_keyword in LOSE_KEYWORDS:
                losses = len(re.findall(f'{char}.*?{lose_keyword}', self.novel.source))
                battles[char]['losses'] += losses

        self.battles = battles
