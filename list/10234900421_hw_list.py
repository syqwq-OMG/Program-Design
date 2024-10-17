# coding = utf-8
# author = syqwq

# 去除这个list中的重复的value,输出处理后的list，并输出重复的元素内容以及重复次数。
list1 = [
    35,
    [3, 2],
    23,
    56,
    32,
    "dd",
    "abc",
    7.24,
    22,
    56,
    22,
    34,
    99,
    "dd",
    [3, 2],
    [4, 6],
    "ABc",
    "abc",
    45,
    78,
    32,
    "a2c",
    "abc",
]

for i in range(len(list1)):
    if type(list1[i]) == list:
        list1[i].sort()
    elif type(list1[i]) == str:
        list1[i] = list1[i].lower()
    else:
        continue

for i in list1[:]:
    cnt = list1.count(i)
    if cnt == 1:
        continue
    print("Item <{}>\t repeated {} times".format(i, cnt))
    for _ in range(cnt - 1):
        list1.remove(i)

print("the UNIQUE list: {}".format(list1))
