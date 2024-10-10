# author : syqwq

if __name__ == "__main__":
    a, b, c, d = map(eval, input().split())
    if a>b and a>c and a>d:
        print("max val: {}".format(a))
    elif b>c and b>d:
        print("max val: {}".format(b))
    elif c>d:
        print("max val: {}".format(c))
    else:
        print("max val: {}".format(d))
