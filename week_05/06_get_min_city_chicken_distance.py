import itertools
import sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_min_city_chicken_distance(n, m, city_map):
    home_location_list = []
    chicken_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize
    for chicken_location_m_combination in chicken_location_m_combinations:
        distance = 0
        for home_r, home_c in home_location_list:
            min_chicken_home_distance = sys.maxsize
            for chicken_r, chicken_c in chicken_location_m_combination:
                min_chicken_home_distance = min(min_chicken_home_distance, abs(home_r - chicken_r)
                                                + abs(home_c - chicken_c))
            distance += min_chicken_home_distance
        min_distance_of_m_combinations = min(distance, min_distance_of_m_combinations)

    return min_distance_of_m_combinations


# 출력
print("정답 = 5 / 현재 풀이 값 = ", get_min_city_chicken_distance(n, m, city_map))

city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5, 1, city_map))

city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5, 2, city_map))
