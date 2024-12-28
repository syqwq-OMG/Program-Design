# 数字三国

Authored by  **孙育泉 10234900421**

## 0x00 准备工作

### 1. 文件结构

```txt
.
├── NDetective.py
├── Novel.py
├── README.md
├── main.py
└── novel.txt
```

- `novel.txt`

  《三国演义》内容存放于  `novel.txt` 中

- `Novel.py`

  考虑有些任务，例如小说的章节数、每章的字数属于小说本身的属性，同时在后续解析文本时，可能需要一些对文本的定位等操作，为此封装了 `Novel` 类，用于处理这类问题

- `Ndetective.py`

  解析文本人物等操作，分封装在 `NDetective` 类中

- `main.py`

  整体集中调用的 `__main__` 函数位于 `main.py` 中

### 2. 库依赖

| 库     | 作用                                                    |
| ------ | ------------------------------------------------------- |
| pandas | 用于统计元素出现次数，类似于python`collections.Counter` |
| jieba  | 用于分析词性，来提取人名                                |

对于 `jieba` 库，也可以使用 `HanLP` 但这次选了`jieba`由于比较易于上手 

## 0x01 Problem 1

> 请显示三国演义所有的回数以及回数标题和该回数的字数

截取出一些标题：

```
正文 第一回 宴桃园豪杰三结义 斩黄巾英雄首立功\n
正文 第二回 张翼德怒鞭督邮 何国舅谋诛宦竖\n
正文 第三回 议温明董卓叱丁原 馈金珠李肃说吕布\n\n
正文 第四回 废汉帝陈留践位 谋董贼孟德献刀\n\n
正文 第五回 发矫诏诸镇应曹公 破关兵三英战吕布\n
......
```

可以发现他们都以**“正文”**开头，以 `\n` 结尾，于是我们可以使用正则表达式，匹配出所有符合要求的字符串。

<u>第一步</u>、根据路径读入文本，并进行文本清洗

``` py
class Novel:
    PUNCTUATIONS = list("，。？、！“”‘’：；《》——-,:.") + ['\ufeff']
    ENDLINE = '\n'

    def __init__(self, path: str):
        self.source = None  # contents of novel
        self.path = path  # path of source
        self.read_novel()

    def clean(self) -> None:
        for sign in Novel.PUNCTUATIONS:
            self.source = self.source.replace(sign, ' ')

    def read_novel(self) -> None:
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
```

可以看到，

| 对象                 | 作用             |
| -------------------- | ---------------- |
| `Novel.PUNCTUATIONS` | 标点常量化       |
| `Novel.ENDLINE`      | 常量化换行符     |
| `novel.source`       | 小说文本内容     |
| `novel.path`         | 文本路径         |
| `novel.clean()`      | 对文本清洗       |
| `novel.read_novel()` | 按照路径读入小说 |

> [!NOTE]
>
> 对于 `class attribute` 我使用大写的类名，对于 `instance attribute` 我使用小写的类名，以下同理。
>
> 代码中的文档注释限于篇幅，已经省去，查看完整代码可以访问 [syqwq-repo](https://github.com/syqwq-OMG/Program-Design/tree/main/novel_detective)

<u>第二步</u>、使用正则表达式进行匹配**标题字符串**

``` py
from typing import List


class Novel:
    def __init__(self, path: str):
        self.titles = self.parse_titles()  # titles of chapters
        self.titles_num = len(self.titles)
  
    def parse_titles(self) -> List[str]:
        import re
        pattern = re.compile('正文[^\\n]{10,30}\\n')
        return list(map(lambda x: x.replace(Novel.ENDLINE, ''), pattern.findall(self.source)))
      
      
    def get_all_titles(self) -> List[str]:
        return self.titles
      
    def get_title_of_chapter(self, index: int) -> str:
        assert 1 <= index <= self.titles_num, 'chapter number out of range'
        return self.titles[index - 1]
```

| 对象                           | 作用                               |
| ------------------------------ | ---------------------------------- |
| `novel.titles`                 | 所有标题                           |
| `novel.titles_num`             | 标题的数目                         |
| `novel.parse_titles()`         | 调用以得到所有标题                 |
| `novel.get_all_titles()`       | 访问所有标题，返回一个字符串列表   |
| `novel.get_title_of_chapter()` | 访问指定章节的标题，序号为自然序号 |

<u>第三步</u>、由于标题之间就是正文，因此可以通过标题来分割所有小说内容，而夹在标题之间的就是正文内容

``` py
class Novel:
    def __init__(self, path: str):
        self.chapters = self.parse_chapters()  # contents of chapters
        assert len(self.titles) == len(self.chapters), 'length of titles and chapters do not match'
        
    def parse_chapters(self) -> List[str]:
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
      
    def get_all_chapters(self) -> List[str]:
        return self.chapters
      
    def get_title_of_chapter(self, index: int) -> str:
        assert 1 <= index <= self.titles_num, 'chapter number out of range'
        return self.titles[index - 1]
```

| 对象                           | 作用                             |
| ------------------------------ | -------------------------------- |
| `novel.chapters`               | 小说所有章节                     |
| `novel.parse_chapters()`       | 得到所有章节                     |
| `novel.get_all_chapters()`     | 访问所有章节，返回一个字符串数组 |
| `novel.get_title_of_chapter()` | 访问指定章节，序号为自然序号     |

至此，第一题已经解决，我们在 `main.py` 中进行调用

``` py
PATH = r'./novel.txt'

if __name__ == '__main__':
    nv = Novel(PATH)

    print('=' * 10 + 'all titles' + '=' * 10)
    for title, chapter in zip(nv.get_all_titles(), nv.get_all_chapters()):
        print(f'{title:<30} \t#words: {len(chapter)}')
```

#### 输出

``` 
==========all titles==========
正文 第一回 宴桃园豪杰三结义 斩黄巾英雄首立功       	#words: 4639
正文 第二回 张翼德怒鞭督邮 何国舅谋诛宦竖         	 #words: 5756
正文 第三回 议温明董卓叱丁原 馈金珠李肃说吕布       	#words: 4966
正文 第四回 废汉帝陈留践位 谋董贼孟德献刀         	#words: 4113
正文 第五回 发矫诏诸镇应曹公 破关兵三英战吕布       	#words: 5602
正文 第六回 焚金阙董卓行凶 匿玉玺孙坚背约         	#words: 4134
正文 第七回 袁绍磐河战公孙 孙坚跨江击刘表         	#words: 4600
正文 第八回 王司徒巧使连环计 董太师大闹凤仪亭       	#words: 4209
正文 第九回 除暴凶吕布助司徒 犯长安李傕听贾诩       	#words: 5313
正文 第十回 勤王室马腾举义 报父仇曹操兴师         	#words: 4189
正文 第十一回 刘皇叔北海救孔融 吕温侯濮阳破曹操      	#words: 5756
正文 第十二回 陶恭祖三让徐州 曹孟穗大战吕布        	#words: 4532
正文 第十三回 李傕郭汜大交兵 杨奉董承双救驾        	#words: 5924
正文 第十四回 曹孟德移驾幸许都 吕奉先乘夜袭徐郡      	#words: 6273
正文 第十五回 太史慈酣斗小霸王 孙伯符大战严白虎      	#words: 7167
正文 第十六回 吕奉先射戟辕门 曹孟德败师淯水        	#words: 6682
正文 第十七回 袁公路大起七军 曹孟德会合三将        	#words: 4325
正文 第十八回 贾文和料敌决胜 夏侯惇拨矢啖睛        	#words: 3766
正文 第十九回 下邳城曹操鏖兵 白门楼吕布殒命        	#words: 6435
正文 第二十回 曹阿瞒许田打围 董国舅内阁受诏        	#words: 4504
......
正文 第一百十一回 邓士载智败姜伯约 诸葛诞义讨司马昭    	#words: 3909
正文 第一百十二回 救寿春于诠死节 取长城伯约鏖兵      	#words: 4051
正文 第一百十三回 丁奉定计斩孙綝 姜维斗阵破邓艾      	#words: 4547
正文 第一百十四回 曹髦驱车死南阙 姜维弃粮胜魏兵      	#words: 3915
正文 第一百十五回 诏班师后主信谗 托屯田姜维避祸      	#words: 4160
正文 第一百十六回 钟会分兵汉中道 武侯显圣定军山      	#words: 4373
正文 第一百十七回 邓士载偷度阴平 诸葛瞻战死绵竹      	#words: 4654
正文 第一百十八回 哭祖庙一王死孝 入西川二士争功      	#words: 3623
正文 第一百十九回 假投降巧计成虚话 再受禅依样画葫芦    	#words: 4956
正文 第一百二十回 荐杜预老将献新谋 降孙皓三分归一统    	#words: 6654
```

## 0x02 Problem 2

> 统计在三国演义中主要人物（自己拟定备选人物，至少10人，尽可能均衡）出现的次数，以及出场顺序，以此认定谁才是三国在演义第一主角

对于一篇文章，可以利用 `jieba` 库中的 `cut` 或者 `lcut` 函数对其进行语义化分，得到的标签为 `nr` 的项就是人名，而考虑到同一个人可能存在称呼不同的情况，例如 诸葛亮也可以称呼为孔明，所以需要人工进行打表合并操作。

``` py
import jieba.posseg as pseg
import pandas as pd
from Novel import *

EXCLUDE_NAMES = ['魏兵', '却说', '将军', '二人', '荆州', '商议', '军士', '军马', '引兵', '次日', '大喜', '曹兵']


class NDetective:
    @staticmethod
    def merge_name(name: str) -> str | None:
        if name in EXCLUDE_NAMES:
            return None
        elif name in (d := ['诸葛亮', '孔明', '孔明曰', '丞相']):
            return d[0]
        elif name in (d := ['刘备', '玄德', '玄德曰']):
            return d[0]
        else:
            return name


    def __init__(self, novel: Novel,
                 character_num: int = 20):
        self.novel = novel
        self.character_num = character_num
        self.characters = self.parse_name_freq()


    def parse_name_freq(self) -> pd.Series:
        names = []
        for word, flag in pseg.cut(self.novel.source, use_paddle=True):
            if flag != 'nr':
                continue
            word = NDetective.merge_name(word)
            if word is not None and len(word) > 1:
                names.append(word)
        return pd.Series(names).value_counts()

    def get_chatacter_freq(self) -> dict[str, int]:
        return dict(self.characters[:self.character_num])
```

| 对象                              | 作用                                                   |
| --------------------------------- | ------------------------------------------------------ |
| `NDetective.merge_name()`         | 人工打表相同的名字                                     |
| `ndetective.novel`                | 读取的小说的来源                                       |
| `ndetective.character_num`        | 需要的主要角色数量，默认 20                            |
| `ndetective.characters`           | 所有的角色                                             |
| `ndetective.parse_name_freq()`    | 得到所有角色的名字和出场次数                           |
| `ndetective.get_chatacter_freq()` | 访问给定主要角色个数的名字和主要个数，按照出场次数排序 |

对于第一次人物出现的章节，可以考虑先找出人物第一次在小说中索引的位置，再通过字数判断人物在第几章节，即使用递归或者循环，每次减去章节的字数和章节的标题。

``` py
class Novel:
    def which_chapter(self, index: int) -> int:
        def helper(idx: int, curr: int) -> int:
            total_words_of_chapter = (len(self.get_content_of_chapter(curr))
                                      + len(self.get_title_of_chapter(curr)))
            if idx <= total_words_of_chapter:
                return curr
            return helper(idx - total_words_of_chapter, curr + 1)
        return helper(index, 1)
```

| 对象                    | 作用                             |
| ----------------------- | -------------------------------- |
| `novel.which_chapter()` | 返回给定索引对应的章节，自然序号 |

在 `main.py` 中进行调用

``` py
from NDetective import *

PATH = r'./novel.txt'


if __name__ == '__main__':
    nvd = NDetective(Novel(PATH), 20)
    nv = nvd.novel

    print('=' * 10 + 'main characters' + '=' * 10)
    characters_freq = nvd.get_chatacter_freq()
    for ch, freq in characters_freq.items():
        first_appear = nv.which_chapter(nv.source.index(ch))
        print(f'Character: {ch:<10}\tFrequency: {freq}\tFirst appear in Chapter: {first_appear}')
```

#### 输出

``` 
==========main characters==========
Character: 诸葛亮       	Frequency: 1373	First appear in Chapter: 37
Character: 刘备        	Frequency: 1068	First appear in Chapter: 1
Character: 曹操        	Frequency: 934	First appear in Chapter: 1
Character: 关公        	Frequency: 509	First appear in Chapter: 1
Character: 张飞        	Frequency: 348	First appear in Chapter: 1
Character: 吕布        	Frequency: 299	First appear in Chapter: 3
Character: 孙权        	Frequency: 264	First appear in Chapter: 15
Character: 赵云        	Frequency: 255	First appear in Chapter: 7
Character: 司马懿       	Frequency: 221	First appear in Chapter: 39
Character: 周瑜        	Frequency: 217	First appear in Chapter: 15
Character: 魏延        	Frequency: 211	First appear in Chapter: 41
Character: 袁绍        	Frequency: 190	First appear in Chapter: 2
Character: 马超        	Frequency: 185	First appear in Chapter: 10
Character: 姜维        	Frequency: 179	First appear in Chapter: 92
Character: 黄忠        	Frequency: 168	First appear in Chapter: 53
Character: 庞德        	Frequency: 122	First appear in Chapter: 35
Character: 张辽        	Frequency: 119	First appear in Chapter: 11
Character: 刘表        	Frequency: 119	First appear in Chapter: 6
Character: 董卓        	Frequency: 114	First appear in Chapter: 1
Character: 徐晃        	Frequency: 113	First appear in Chapter: 13
```

## 0x03 Problem 3

> 请输出在备选人物中，用数据说话谁和谁关系最铁

我的理解就是统计在给定的上下文环境下，两个人互动即共同出现的次数。而对于给定的上下文，可以看对于每个章节而言进行选取，也可以根据换行符进行分割，对于每一行作为一个上下文。

在此提供了以上两个策略，对于其他的上下文方法，可以自行探索。

``` py
from collections import defaultdict, OrderedDict


CHAPTER_AS_A_WHOLE = lambda x: x
SPLIT_LINES = lambda x: x.split('\n')

def iterate(obj):
    if not isinstance(obj, list):
        return [obj]

    ret = []
    for x in obj:
        ret += iterate(x)
    return ret


class NDetective:
    def __init__(self, novel: Novel,
                 character_num: int = 20,
                 parse_relation_strategy=CHAPTER_AS_A_WHOLE):

        self.strategy = parse_relation_strategy
        self.relationships = defaultdict(int)
        self.parse_relations()
        
    @staticmethod
    def count_occurance_in_context(per1: str, per2: str, context: str) -> int:
        return min(context.count(per1), context.count(per2))

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
```

| 对象                                      | 作用                                                         |
| ----------------------------------------- | ------------------------------------------------------------ |
| `NDetective.count_occurance_in_context()` | 统计两个角色在同一上下文下出现的次数                         |
| `ndetective.strategy`                     | 对于上下文的生成策略，在此提供两种：`CHAPTER_AS_A_WHOLE` , `SPLIT_LINES` |
| `ndetective.relationships`                | 人物关系，即在同一上下文中，共同出现的次数，`key` 为主要角色的有序笛卡尔积，`value` 为出现次数 |
| `ndetective.parse_relations()`            | 统计人物关                                                   |

由于每次判断 `dict` 的 `key` 是否出现过赋初始值较为麻烦，考虑使用 `collections` 库中的 `defaultdict` 

由于python中的 `dict` 本身不支持排序，所以使用 `collections.OrderedDict`

因为 python 字典不支持切片操作，所以考虑使用迭代器语法。

在 `main.py` 中进行调用

``` py
from NDetective import *

PATH = r'./novel.txt'

if __name__ == '__main__':
    nvd = NDetective(Novel(PATH), 20, parse_relation_strategy=CHAPTER_AS_A_WHOLE)
    nv = nvd.novel
    print('=' * 10 + 'TOP 10 closest relationship' + '=' * 10)
    it = iter(nvd.relationships.items())
    for i in range(1, 11):
        (ch1, ch2), cnt = next(it)
        print(f'TOP {i}:\t {ch1}<-->{ch2} \t interacts {cnt} times')
```

#### 输出

``` 
==========TOP 10 closest relationship==========
TOP 1:	 刘备<-->曹操 	 interacts 230 times
TOP 2:	 曹操<-->张飞 	 interacts 202 times
TOP 3:	 曹操<-->袁绍 	 interacts 201 times
TOP 4:	 曹操<-->孙权 	 interacts 196 times
TOP 5:	 曹操<-->吕布 	 interacts 174 times
TOP 6:	 曹操<-->赵云 	 interacts 148 times
TOP 7:	 曹操<-->周瑜 	 interacts 135 times
TOP 8:	 刘备<-->张飞 	 interacts 126 times
TOP 9:	 曹操<-->张辽 	 interacts 126 times
TOP 10:	 曹操<-->关公 	 interacts 120 times
```

## 0x04 Problem 4

> 请输出备选人物中，战绩情况，赢几次，输几次

对于这个问题，好像可以使用对文法结构分析后使用 `SnowNLP` 进行情感分析？ 但我不会啊。

所以，我依然使用正则表达式进行匹配。可以手动枚举一些表示胜负的词语，然后对于主要角色以及这些词语的组合进行正则表达式匹配。

``` py
WIN_KEYWORDS = ['胜', '大胜', '胜利', '战胜', '取胜', '成功', '克敌制胜', '击败', '夺取', '打败']
LOSE_KEYWORDS = ['败', '败北', '失败', '落败', '溃败', '败阵', '败退', '失败', '败逃']


class NDetective:
    def __init__(self, novel: Novel,
                 character_num: int = 20,
                 parse_relation_strategy=CHAPTER_AS_A_WHOLE):
        self.battles = dict()
        self.parse_battles()

    def parse_battles(self):
        battles = {char: {'wins': 0, 'losses': 0} for char in self.get_chatacter_freq().keys()}

        for char in self.get_chatacter_freq().keys():
            for win_keyword in WIN_KEYWORDS:
                wins = len(re.findall(f'{char}.*?{win_keyword}', self.novel.source))
                battles[char]['wins'] += wins

            for lose_keyword in LOSE_KEYWORDS:
                losses = len(re.findall(f'{char}.*?{lose_keyword}', self.novel.source))
                battles[char]['losses'] += losses

        self.battles = battles
```

| 对象                         | 作用                               |
| ---------------------------- | ---------------------------------- |
| `ndetective.battles`         | 所有主要角色名字、赢和输组成的字典 |
| `ndetective.parse_battles()` | 得到`battles`的函数                |

``` py
# coding = utf-8
# author = syqwq

from NDetective import *

PATH = r'./novel.txt'

if __name__ == '__main__':
    nvd = NDetective(Novel(PATH), 20, parse_relation_strategy=CHAPTER_AS_A_WHOLE)
    nv = nvd.novel
    
		print('=' * 10 + 'WIN or LOSE' + '=' * 10)
    battles = nvd.battles
    for ch in battles.keys():
        print(f'{ch:<5}\t WIN: {battles[ch]['wins']:<7}\t LOSE: {battles[ch]['losses']}')
```

在 `main.py` 中进行调用

#### 输出

``` 
==========WIN or LOSE==========
诸葛亮  	 WIN: 32     	 LOSE: 29
刘备   	 WIN: 41     	 LOSE: 24
曹操   	 WIN: 107    	 LOSE: 101
关公   	 WIN: 19     	 LOSE: 22
张飞   	 WIN: 33     	 LOSE: 47
吕布   	 WIN: 30     	 LOSE: 33
孙权   	 WIN: 42     	 LOSE: 25
赵云   	 WIN: 40     	 LOSE: 45
司马懿  	 WIN: 47     	 LOSE: 41
周瑜   	 WIN: 26     	 LOSE: 16
魏延   	 WIN: 44     	 LOSE: 56
袁绍   	 WIN: 43     	 LOSE: 44
马超   	 WIN: 22     	 LOSE: 23
姜维   	 WIN: 43     	 LOSE: 41
黄忠   	 WIN: 21     	 LOSE: 31
庞德   	 WIN: 11     	 LOSE: 11
张辽   	 WIN: 22     	 LOSE: 21
刘表   	 WIN: 19     	 LOSE: 23
董卓   	 WIN: 9      	 LOSE: 17
徐晃   	 WIN: 21     	 LOSE: 20
```

## 0xFF idk

- 源代码位于

  [https://github.com/syqwq-OMG/Program-Design/tree/main/novel_detective](https://github.com/syqwq-OMG/Program-Design/tree/main/novel_detective)
  
  
