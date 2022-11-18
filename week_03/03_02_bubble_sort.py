input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    index = len(array)-1
    while index != 0:
        for i in range(index):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        index -= 1
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
