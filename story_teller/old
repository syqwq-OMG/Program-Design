with open("news.txt", encoding="utf-8", mode="r") as f:
    source = f.read()

### Task 1
token_len = int(input("input split length: "))
# token_len = 2

source, puncs = source.lower(), '-.*?!”"“,'
for punc in puncs:
    source = source.replace(punc, "")
source = source.split()
tokens = [tuple(source[i : i + token_len]) for i in range(len(source) - token_len + 1)]
# print(tokens)
print("=" * 15)

### Task 2
token_freq = {}
for token in tokens:
    token_freq.setdefault(token, tokens.count(token))

### Task 3
from random import choice

passage_len = int(input("expected passage length: "))
print("=" * 15)
bg_token = choice(tokens)
print("passage start with <{}>:\n{}".format(bg_token, " ".join(bg_token)), end=" ")
output = " ".join(bg_token) + " "

last_words = bg_token[1:]
for _ in range(passage_len - 1):
    # all tokens begin with last_word
    toks_bg_with_lws = [
        token for token in tokens if token[: token_len - 1] == last_words
    ]

    assert (
        len(toks_bg_with_lws) != 0
    ), "CANNOT continue with this bg_token: <{}>".format(bg_token)

    # sort the tokens with their freq
    toks_bg_with_lws.sort(key=lambda token: token_freq[token])
    top_freq = token_freq[toks_bg_with_lws[0]]

    # pick out all top_freq lw_keys
    toks_bg_with_lws = [
        tbwl for tbwl in toks_bg_with_lws if token_freq[tbwl] == top_freq
    ]
    last_words = choice(toks_bg_with_lws)[1:]  # update last_words
    output += " " + last_words[-1]

print(output)


### Task 4
def word_p(word: str, lib: list, SIG=0.1):
    """
    calculate the frequency of word in source lib

    word:   the word
    lib:    source lib
    SIG:    constant
    """
    V = len(set(lib))
    return (lib.count(word) + SIG) / (len(lib) + SIG * V)


def word_cond_p(word1: str, words: tuple, tokens: list, SIG=0.1):
    V = len(set(tokens))
    return (tokens.count((word1, *words)) + SIG) / (len(tokens) + SIG * V)


def sentence_prob(sentence:str, lib:list,SIG=0.1):
    prob=1.0
    for w in sentence:
        prob*=word_p(w,lib,SIG)
    return prob