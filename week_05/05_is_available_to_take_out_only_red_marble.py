from collections import deque
from typing import List

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# #E W S N
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]


# def switch_loc(marble: List[int], d: int) -> List[int]:
#     marble[0] = marble[0] + dx[d]
#     marble[1] = marble[1] + dy[d]
#     return marble
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0
    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "O":
        r = r + diff_r
        c = c + diff_c
        move_count += 1
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map: List[List]) -> bool:
    # red, blue = [], []
    # hole = []
    # queue = collections.deque()
    # for i, squares in enumerate(game_map):
    #     for j, square in enumerate(squares):
    #         if not red and not blue and hole:
    #             break
    #         if square == "R":
    #             red = [i, j]
    #         elif square == "B":
    #             blue = [i, j]
    #         elif square == "O":
    #             hole = [i, j]
    # queue.append([red, blue])
    #
    # for i in range(10):
    #     r, b = queue.popleft()
    #     if r == hole:
    #         return True
    #     for j in range(4):
    #         new_r = switch_loc(r, j)
    #         new_b = switch_loc(b, j)
    #         queue.append([new_r, new_b])
    #
    # return False
    n, m = len(game_map), len(game_map[0])
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break
        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)
            if game_map[next_blue_row][next_blue_col] == "O":
                continue
            if game_map[next_red_row][next_red_col] == "O":
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if r_count > b_count:
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]

            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True ??? ???????????? ?????????

game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("?????? = False / ?????? ?????? ??? = ", is_available_to_take_out_only_red_marble(game_map))

game_map = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", "R", "#", "B", "#"],
    ["#", ".", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", ".", "#"],
    ["#", "O", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]
print("?????? = True / ?????? ?????? ??? = ", is_available_to_take_out_only_red_marble(game_map))
