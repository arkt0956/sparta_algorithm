from typing import List

array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1: List[int], array2: List[int]) -> List[int]:
    pointer_1, pointer_2 = 0, 0
    array = []
    
    while pointer_1 < len(array1) and pointer_2 < len(array2):
        if array1[pointer_1] < array2[pointer_2]:
            array.append(array1[pointer_1])
            pointer_1 += 1
        else:
            array.append(array2[pointer_2])
            pointer_2 += 1

    if pointer_1 < len(array1):
        for element in array1[pointer_1:]:
            array.append(element)
    elif pointer_2 < len(array2):
        for element in array2[pointer_2:]:
            array.append(element)

    return array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!
