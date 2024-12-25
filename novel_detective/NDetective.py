import jieba.posseg as pseg
import pandas as pd
from Novel import *

EXCLUDE_NAMES = ['魏兵', '却说', '将军', '二人', '荆州', '商议', '军士', '军马', '引兵', '次日', '大喜', '曹兵']


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

    def __init__(self, novel: Novel):
        self.novel = novel
        self.characters = self.parse_name_freq()

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

    def parse_battles(self):
        pass

    def parse_relations(self):
        pass
