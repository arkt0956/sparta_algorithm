finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    current_min, current_max = 0, len(array) - 1

    while current_min <= current_max:
        center = (current_min + current_max) // 2
        if array[center] == target:
            print("target: ", target)
            print("찾은 값: ", array[center])
            return True
        elif array[center] < target:
            current_min = center + 1
        else:
            current_max = center - 1

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
