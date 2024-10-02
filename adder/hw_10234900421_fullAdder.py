# coding: utf-8
# author: syqwq

s, c_in, ans = 0, 0, 0

if __name__ == "__main__":
    a0 = eval(input("A0="))
    a1 = eval(input("A1="))
    b0 = eval(input("B0="))
    b1 = eval(input("B1="))

    s = a0 ^ b0 ^ c_in
    ans |= s << 0
    c_in = (a0 & b0) | ((a0 ^ b0) & c_in)

    s = a1 ^ b1 ^ c_in
    ans |= s << 1
    c_in = (a1 & b1) | ((a1 ^ b1) & c_in)

    ans |= c_in << 2

    print("%d%d+%d%d=" % (a1, a0, b1, b0), end="")
    if ans >> 2:
        print("%d%d%d\n" % (ans >> 2, (ans >> 1) & 1, ans & 1))
    else:
        print("%d%d\n" % ((ans >> 1) & 1, ans & 1))
