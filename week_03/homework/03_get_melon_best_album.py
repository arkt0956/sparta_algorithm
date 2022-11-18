import collections
from typing import List

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

genres1 = ["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"]
plays1 = [2000, 500, 600, 150, 800, 2500, 2000]


def get_melon_best_album(genre_array, play_array) -> List[int]:
    result = []
    dicts = collections.defaultdict(list)
    order_dicts = collections.defaultdict(int)
    for i in range(len(genre_array)):
        order_dicts[genre_array[i]] += play_array[i]
        dicts[genre_array[i]].append([i, play_array[i]])

    order_dicts = sorted(order_dicts.items(), key=lambda item: item[1], reverse=True)

    for k, v in order_dicts:
        temp: List = sorted(dicts[k], key=lambda item: item[1], reverse=True)
        if len(temp) >= 2:
            for element in temp[:2]:
                result.append(element[0])
        else:
            for element in temp:
                result.append(element[0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
print(get_melon_best_album(genres1, plays1))  # 정답 = [0, 6, 5, 2, 4, 1]
