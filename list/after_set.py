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

print("the ORIGINAL list: {}".format(list1))

for i in range(len(list1)):
    if type(list1[i]) == list:
        """
        Sets require their items to be hashable. Out of types predefined by Python only the immutable ones, such as strings, numbers, and tuples, are hashable. Mutable types, such as lists and dicts, are not hashable because a change of their contents would change the hash and break the lookup code.
        """
        list1[i] = tuple(sorted(list1[i]))
    elif type(list1[i]) == str:
        list1[i] = list1[i].lower()
    else:
        continue

list1 = set(list1)

print("the UNIQUE list: {}".format(list(list1)))
