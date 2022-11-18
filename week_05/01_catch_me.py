import collections
from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc) -> int:
    queue = deque()
    queue.append((brown_loc, 0))
    time = 0
    visited = collections.defaultdict(dict)

    while cony_loc < 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time

        for i in range(len(queue)):
            current_position, current = queue.popleft()

            next_time = current + 1
            next_position = current_position + 1
            if next_position <= 200000 and next_time not in visited[next_position]:
                visited[next_position][next_time] = True
                queue.append((next_position, next_time))

            next_position = current_position - 1
            if next_position >= 0 and next_time not in visited[next_position]:
                visited[next_position][next_time] = True
                queue.append((next_position, next_time))

            next_position = current_position * 2
            if next_position <= 200000 and next_time not in visited[next_position]:
                visited[next_position][next_time] = True
                queue.append((next_position, next_time))

        time += 1



print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))
