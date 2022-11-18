# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []


def dfs_recursion(adjacent_graph, cur_node, visited_array):
    if not visited_array:
        visited_array.append(1)

    for element in adjacent_graph[cur_node]:
        count: int = 0
        print("현재 노드: ", element)
        if element not in visited_array:
            cur_node = element
            visited_array.append(element)
            print("visit: ", visited_array)
            dfs_recursion(adjacent_graph, cur_node, visited_array)
        else:
            count += 1
            if count == len(adjacent_graph[cur_node]):
                continue


dfs_recursion(graph, 1, visited)  # 1 이 시작 노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
