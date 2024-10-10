# author = syqwq
# coding = utf-8


if __name__ == "__main__":
    ans = 0

    zero = 0
    jan = zero + 31
    feb = jan + 28

    yy = eval(input("input year: "))

    if (yy % 100 == 0 and yy % 400 == 0) or (yy % 100 != 0 and yy % 4 == 0):
        feb += 1

    march = feb + 31
    april = march + 30
    may = april + 31
    june = may + 30
    july = june + 31
    aug = july + 31
    sept = aug + 30
    oct = sept + 31
    nov = oct + 30

    mm = eval(input("input month: "))
    dd = eval(input("input day: "))

    if mm == 1:
        ans += zero
    elif mm == 2:
        ans += jan
    elif mm == 3:
        ans += feb
    elif mm == 4:
        ans += march
    elif mm == 5:
        ans += april
    elif mm == 6:
        ans += may
    elif mm == 7:
        ans += june
    elif mm == 8:
        ans += july
    elif mm == 9:
        ans += aug
    elif mm == 10:
        ans += sept
    elif mm == 11:
        ans += oct
    else:
        ans += nov

    ans += dd

    print("{}-{}-{} is the {} th day of the year".format(yy, mm, dd, ans))
