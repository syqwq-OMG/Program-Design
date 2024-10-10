# author = syqwq
# coding = utf-8

if __name__ == '__main__':
    a, b, c = (int(i) for i in input().split())

    if a + b > c and b + c > a and c + a > b:
        print("the perimeter of the triangle is: {}".format(a + b + c))
    else:
        print("CANNOT make up a triangle")
