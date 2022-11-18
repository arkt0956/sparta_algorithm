input = [4, 6, 2, 9, 1]


def selection_sort(array):
    min_value_index = 0
    index = 0
    while index != len(array)-1:
        for i in range(index, len(array)):
            if array[min_value_index] > array[i]:
                min_value_index = i
        array[min_value_index], array[index] = array[index], array[min_value_index]
        index += 1

    return array


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
