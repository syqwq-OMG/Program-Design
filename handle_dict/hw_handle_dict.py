# author: syqwq


stu_score = {
    "zhangsan": "98.123",
    "lisi": "58.456",
    "wangwu": "67.986",
    "laowang": 99.22,
    "xiaoxia": "57.333",
    "liming": "Null",
    "zhangjin": "154.213",
    "jingsong": "-24.345",
    "liusong": "",
    "niuniu": "Null",
    "lili": -13.123,
}


def is_number(x):
    try:
        float(x)
    except:
        return False
    else:
        return True


def handle(dic, num):
    return {
        k: round(float(v), num)
        for k, v in filter(lambda x: is_number(x[1]), dic.items())
    }


if __name__ == "__main__":
    print(handle(stu_score, 2))
