# author: syqwq
# coding: utf-8

scores = {
    "语文": [86, 97, 98, 77, 92, 94, 99, 97],
    "数学": [92, 91, 93, 88, 96, 91, 91, 88],
    "英语": [100, 96, 94, 60, 97, 92, 93, 86],
}
names = ["太史慈", "臧霸", "张角", "曹真", "王朗", "马谡", "姜维", "徐庶"]


def mean(l: list):
    return sum(l) / len(l)


def mean_max(subject: str) -> None:
    sub_scores = scores[subject]
    sub_mean = mean(sub_scores)
    sub_max = max(zip(names, sub_scores), key=lambda x: x[1])[0]
    print(f"{subject}课的平均成绩{sub_mean},\t最高分姓名: {sub_max}")


def conv(sub1: str, sub2: str) -> None:
    s1, s2 = scores[sub1], scores[sub2]
    assert len(s1) == len(s2), "length of two subjects score is not equal"
    l = len(s1)

    s1m, s2m = mean(s1), mean(s2)
    tmp1, tmp2 = map(lambda x: x - s1m, s1), map(lambda x: x - s2m, s2)
    ans = sum(map(lambda x: x[0] * x[1], zip(tmp1, tmp2))) / (l - 1)
    print(f"{sub1}与{sub2}的协方差是{ans}")


if __name__ == "__main__":
    for sub in scores.keys():
        mean_max(sub)
    conv("语文", "数学")
    conv("英语", "数学")
    conv("语文", "英语")
