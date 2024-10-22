# coding = utf-8
# author = syqwq
vote1 = [
    "柴进",
    "卢俊义",
    "柴进",
    "柴进",
    "柴进",
    "柴进",
    "卢俊义",
    "柴进",
    "弃权",
    "卢俊义",
    "柴进",
    "柴进",
    "卢俊义",
    "柴进",
    "卢俊义",
    "卢俊义",
    "弃权",
]
vote2 = [
    "卢俊义",
    "柴进",
    "柴进",
    "董平",
    "卢俊义",
    "卢俊义",
    "柴进",
    "弃权",
    "武松",
    "史进",
    "柴进",
    "卢俊义",
    "柴进",
    "林冲",
    "卢俊义",
    "弃权",
    "弃权",
]
vote3 = [
    "卢俊义",
    "柴进",
    "柴进",
    "柴进",
    "卢俊义",
    "吴用",
    "林冲",
    "卢俊义",
    "柴进",
    "柴进",
    "弃权",
    "史进",
    "吴用",
    "卢俊义",
    "柴进",
    "林冲",
    "宋江",
    "宋江",
    "卢俊义",
    "弃权",
    "弃权",
]
vote4 = [
    "鲁智深",
    "弃权",
    "花荣",
    "弃权",
    "林冲",
    "弃权",
    "弃权",
    "史进",
    "吴用",
    "弃权",
    "柴进",
    "弃权",
    "宋江",
    "宋江",
    "卢俊义",
    "弃权",
    "弃权",
]
vote_all = [vote1, vote2, vote3, vote4]

vote_valid_groups, valid_votes = [], []
invalid = "弃权"
candidates, promoted, names_rates_nums = set(), [], {}

for vote_group in vote_all:
    if 3 * vote_group.count(invalid) <= len(vote_group):
        vote_valid_groups.append(vote_group)
    valid_votes += [vote for vote in vote_group if vote != invalid]

candidates = set(valid_votes)
for candidate in list(candidates):
    candidate_vote_num = valid_votes.count(candidate)
    candidate_vote_rate = candidate_vote_num / len(valid_votes)
    names_rates_nums[candidate] = (candidate_vote_rate, candidate_vote_num)

    if (
        len([vg for vg in vote_valid_groups if candidate in vg]) >= 2
        and candidate_vote_rate > 0.35
    ):
        promoted.append(candidate)


print("晋级名单:", promoted)
for name, (rate, num) in names_rates_nums.items():
    print(
        "=" * 10,
        "\n",
        "NAME:\t{}\n".format(name),
        "RATE:\t{:.2f}%\n".format(rate * 100),
        "VOTE:\t{}".format(num),
    )
