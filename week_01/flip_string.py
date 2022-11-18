input = "1101000010"


def find_count_to_turn_out_to_all_zero_or_all_one(string: str) -> int:
    count_to_one = 0
    count_to_zero = 0

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            if string[i] == "1":
                count_to_zero += 1

            if string[i] == "0":
                count_to_one += 1

    if string[-1] != string[-2]:
        if string[-1] == "0":
            count_to_one += 1

        elif string[-1] == "1":
            count_to_zero += 1
    return min(count_to_zero, count_to_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
