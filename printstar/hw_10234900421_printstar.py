# author = syqwq
# coding = utf-8

if __name__ == "__main__":
    lines = int(input("Please input the line: "))

    for i in range(1, lines + 1):
        for _ in range(lines - i + 1):
            print(" ", end="")
        for _ in range(2 * i - 1):
            print("*", end="")
        print()
        
    for i in range(lines, 0, -1):
        for _ in range(lines - i + 1):
            print(" ", end="")
        for _ in range(2 * i - 1):
            print("*", end="")
        print()
