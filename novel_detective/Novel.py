from typing import List


class Novel:
    PUNCTUATIONS = list("，。？、！“”‘’：；《》——-,:.") + ['\ufeff']
    ENDLINE = '\n'

    def __init__(self, path: str):
        """
        init a Novel object
        :param path: the path to the novel file
        """
        self.source = None  # contents of novel
        self.path = path  # path of source
        self.read_novel()

        self.titles = self.parse_titles()  # titles of chapters
        self.titles_num = len(self.titles)
        self.chapters = self.parse_chapters()  # contents of chapters

        assert len(self.titles) == len(self.chapters), 'length of titles and chapters do not match'

    def clean(self) -> None:
        """
        clean some punctuation of the source
        :return: a text without punctuation detaminated
        """
        for sign in Novel.PUNCTUATIONS:
            self.source = self.source.replace(sign, ' ')

    def read_novel(self) -> None:
        """
        read the content of given path and return novel content
        :return: the content of novel
        """
        import os

        if not os.path.exists(self.path):
            raise FileNotFoundError(f'{self.path} is not exist')

        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                self.source = f.read()
        except Exception as e:
            print(f'Error: {e} occurred')
        else:
            self.clean()

    def parse_titles(self) -> List[str]:
        """
        parse the content of given path and return novel titles of each chapter
        :return: a list of novel titles
        """
        import re

        pattern = re.compile('正文[^\\n]{10,30}\\n')
        return list(map(lambda x: x.replace(Novel.ENDLINE, ''), pattern.findall(self.source)))

    def parse_chapters(self) -> List[str]:
        """
        parse the content of given path and return novel chapters contents of each chapter
        :return: a list of novel chapters contents
        """
        contents = []

        for idx in range(1, self.titles_num):  # special judge for the last chapter
            ith_title = self.get_title_of_chapter(idx)
            i1_title = self.get_title_of_chapter(idx + 1)
            start = self.source.index(ith_title) + len(ith_title)
            end = self.source.index(i1_title)
            contents.append(self.source[start:end])  # start -> end - 1

        last_title = self.get_title_of_chapter(self.titles_num)
        start = self.source.index(last_title) + len(last_title)
        contents.append(self.source[start:])

        return contents

    def get_title_of_chapter(self, index: int) -> str:
        """
        get the novel title of a given chapter number
        :param index: the novel chapter number starting from 1 to 120
        :return: the novel title of a given chapter number
        """
        assert 1 <= index <= self.titles_num, 'chapter number out of range'

        return self.titles[index - 1]

    def get_content_of_chapter(self, index: int) -> str:
        """
        get the novel chapter content of a given novel chapter number
        :param index: the novel chapter number starting from 1 to 120
        :return: the novel chapter content of a given novel chapter number
        """
        assert 1 <= index <= self.titles_num, 'chapter number out of range'

        return self.chapters[index - 1]

    def get_all_titles(self) -> List[str]:
        """
        get the novel titles of all chapters
        :return: all novel titles
        """
        return self.titles

    def get_all_chapters(self) -> List[str]:
        """
        get the novel chapters of all chapters
        :return: get all novel chapters
        """
        return self.chapters

    def which_chapter(self, index: int) -> int:
        """
        get the novel chapter of a given index of letter
        :param index: a word index
        :return: the novel chapter of a given index
        """

        def helper(idx: int, curr: int) -> int:
            total_words_of_chapter = (len(self.get_content_of_chapter(curr))
                                      + len(self.get_title_of_chapter(curr)))
            if idx <= total_words_of_chapter:
                return curr
            return helper(idx - total_words_of_chapter, curr + 1)

        return helper(index, 1)

    def __str__(self):
        return self.source

    def __repr__(self):
        return 'Novel({})'.format(self.path.__repr__())
