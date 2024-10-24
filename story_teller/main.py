from random import choice, choices
from collections import Counter
from typing import List, Tuple


def clean2tokens(s: str, tklen: int = 2) -> List[Tuple[str, ...]]:
    s = s.lower()
    punctuations = '-*?!”"“.;,()'
    for punc in punctuations:
        s = s.replace(punc, "")
    s = s.split()
    tks = [tuple(s[i: i + tklen]) for i in range(len(s) - tklen + 1)]
    return tks


def generate(s: str, tklen: int, psglen: int) -> str:
    tokens = clean2tokens(s, tklen)
    token_freq = Counter(tokens)

    bg_token = choice(tokens)
    output = ' '.join(bg_token)

    last_words = bg_token[1:]  # Get the last words to form the context
    for _ in range(psglen - 1):
        tks_bg_with_lw = [tk for tk in tokens if tk[:-1] == last_words]

        if not tks_bg_with_lw:
            break  # If no further tokens, stop the generation.

        # Sort and select based on frequency
        tks_bg_with_lw.sort(key=lambda tk: token_freq[tk], reverse=True)

        # Introduce some randomness in selection
        top_freq = token_freq[tks_bg_with_lw[0]]
        weighted_choices = [tk for tk in tks_bg_with_lw if token_freq[tk] >= top_freq // 2]
        next_token = choices(weighted_choices, weights=[token_freq[tk] for tk in weighted_choices])[0]

        last_words = next_token[1:]  # Update last words
        output += ' ' + last_words[-1]  # Add the next word to output

    return output


if __name__ == '__main__':
    with open('news.txt', encoding='utf-8', mode='r') as f:
        source = f.read()

    for _ in range(20):
        token_len, passage_len = 3, 50
        output_passage = generate(source, token_len, passage_len)
        print(output_passage)
        print('=' * 15)
