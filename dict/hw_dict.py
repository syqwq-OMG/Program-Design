d = {}

PROMPT = """===============
请选择功能：
1: 输入
2: 查找
3: 退出
"""
PROMPT_INPUT = [
    "请输入英文单词（按回车结束）：",
    "请输入中文翻译：",
    "该单词已添加到字典库。",
]
PROMPT_QUERY = [
    "请输入要查询的内容（按回车结束）：",
    "{}的中文翻译是{}",
    "{}的英文翻译是{}",
]
PROMPT_ERROR = "out of RANGE!"

while True:
    opt = int(input(PROMPT))
    if opt == 3:
        break
    elif opt == 1:
        en, zh = input(PROMPT_INPUT[0]).lower(), input(PROMPT_INPUT[1])
        d[en], d[zh] = (zh, 1), (en.capitalize(), 2)
        print(PROMPT_INPUT[2])
    elif opt == 2:
        q = input(PROMPT_QUERY[0]).lower()
        result = d.get(q, None)
        if result:
            print(PROMPT_QUERY[result[1]].format(q, result[0]))
        else:
            print(PROMPT_ERROR)
    else:
        print(PROMPT_ERROR)
