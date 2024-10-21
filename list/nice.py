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
    # "abc",
    "ABc",
    7.24,
    22,
    56,
    22,
    34,
    99,
    "dd",
    [3, 2],
    [4, 6],
    "Abc",
    # "abc",
    45,
    78,
    32,
    "a2c",
    # "abc",
]

print("the ORIGINAL list: {}".format(list1))

list1=[val for i,val in enumerate(list1) if not any(
    (lambda x,y: False if type(x)!=type(y) else (lambda x,y: x.lower()==y.lower() if type(x)==str else (lambda x,y: sorted(x)==sorted(y) if type(x)==list else (lambda x,y: x==y)(x,y))(x,y))(x,y))(val,t) for t in list1[:i]
)]

print("the UNIQUE list: {}".format(list1))
