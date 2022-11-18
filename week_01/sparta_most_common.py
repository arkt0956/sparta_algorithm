import collections
import re

input = "hello my name is sparta"


def find_max_occurred_alphabet(words: str) -> str:
    words = words.replace(" ", "")
    dicts = collections.defaultdict(int)
    for word in words:
        dicts[word] += 1

    # max = collections.Counter(words)
    # return max.most_common(1)[0][0]
    maximum = max(dicts, key=dicts.get)

    return maximum


result = find_max_occurred_alphabet(input)
print(result)
