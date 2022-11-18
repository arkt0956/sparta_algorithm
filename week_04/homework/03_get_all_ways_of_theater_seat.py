seat_count = 9
vip_seat_array = [4, 7]
memo = {
    1: 1,
    2: 2,
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        print("memo: ", memo)
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    print("memo: ", memo)
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array) -> int:
    count = 1
    current = 0
    for vip in fixed_seat_array:
        count *= fibo_dynamic_programming(vip - 1 - current, memo)
        current = vip
    count *= fibo_dynamic_programming(total_count - current, memo)

    return count


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [2, 4, 7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11, [2, 5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10, [2, 6, 9]))
