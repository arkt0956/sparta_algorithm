import time

top_heights = [6, 9, 5, 7, 4]

start_time = time.time()


def get_receiver_top_orders(heights):
    result = []

    while heights:
        h = heights.pop()
        for height in range(len(heights)-1, -1, -1):
            if heights[height] > h:
                result.append(height+1)
                break
        else:
            result.append(0)

    return result[::-1]


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders([6, 9, 5, 7, 4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ", get_receiver_top_orders([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ", get_receiver_top_orders([1, 5, 3, 6, 7, 6, 5]))

print("성능 :", time.time() - start_time)
