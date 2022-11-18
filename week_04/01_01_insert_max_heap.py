class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value) -> None:
        if self.items == [None]:
            self.items.append(value)
        else:
            current = len(self.items)   # value가 추가되기 전에 계산해서 -1 연산을 안 하도록 한다.
            self.items.append(value)
            while self.items[current // 2] < self.items[current]:
                self.items[current // 2], self.items[current] = self.items[current], self.items[current // 2]
                current = current // 2
                if current == 1:
                    return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!