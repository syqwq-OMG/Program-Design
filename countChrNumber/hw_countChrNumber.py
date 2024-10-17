# coding = utf-8
# author = syqwq
kinds = ["UPPERcase", "LOWERcase", "Number", "Other"]
char_classified = [[], [], [], []]
char_cnt = [0] * 4

s = input("input a random string: ")

for ch in s:
    idx = 0
    if ch in list("1234567890"):
        idx = 2
    elif ch in [chr(i) for i in range(ord("a"), ord("z") + 1)]:
        idx = 1
    elif ch in [chr(i) for i in range(ord("A"), ord("Z") + 1)]:
        idx = 0
    else:
        idx = 3
    char_cnt[idx] += 1
    char_classified[idx].append(ch)

for i in range(4):
    print("{}: {}".format(kinds[i], char_cnt[i]))

max_idx = char_cnt.index(max(char_cnt))
print(
    "{} appears most, seperately are: {}".format(
        kinds[max_idx], char_classified[max_idx]
    )
)
