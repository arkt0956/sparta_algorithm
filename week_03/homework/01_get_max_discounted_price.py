from typing import List

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def merge(array1: List[int], array2: List[int]) -> List[str]:
    result = []
    pointer_1, pointer_2 = 0, 0
    while pointer_1 < len(array1) and pointer_2 < len(array2):
        if array1[pointer_1] > array2[pointer_2]:
            result.append(array1[pointer_1])
            pointer_1 += 1
        else:
            result.append(array2[pointer_2])
            pointer_2 += 1

    if pointer_1 < len(array1):
        for element in array1[pointer_1:]:
            result.append(element)
    if pointer_2 < len(array2):
        for element in array2[pointer_2:]:
            result.append(element)
    return result


def merge_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array
    mid: int = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array,right_array)


def get_max_discounted_price(prices, coupons):
    prices = merge_sort(prices)
    coupons = merge_sort(coupons)

    pointer = 0
    total = 0
    while pointer < len(prices) and pointer < len(coupons):
        total += prices[pointer] * ((100- coupons[pointer]) * 0.01)
        pointer += 1

    if pointer < len(prices):
        for item in prices[pointer:]:
            total += item
    return int(total)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
