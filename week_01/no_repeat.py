import collections

input = "abadabac"


def find_not_repeating_character(string: str) -> str:
    dic = collections.defaultdict(int)
    for char in string:
        dic[char] += 1
    for key, value in dic.items():
        if value == 1:
            return key
    return "_"


result = find_not_repeating_character(input)
print(result)
