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

    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        del_element = self.items.pop()

        current = 1
        # while current*2 < len(self.items):
        #     if current*2+1 > len(self.items):
        #         print(current)
        #         if self.items[current] < self.items[current*2]:
        #             self.items[current], self.items[current * 2] = self.items[current * 2], self.items[current]
        #             current = current * 2
        #     else:
        #         if self.items[current] < self.items[current*2] or self.items[current] < self.items[current*2+1]:
        #             if self.items[current*2] > self.items[current*2+1]:
        #                 self.items[current], self.items[current*2] = self.items[current*2], self.items[current]
        #                 current = current*2
        #             else:
        #                 self.items[current], self.items[current * 2+1] = self.items[current * 2+1], self.items[current]
        #                 current = current*2 + 1
        while current < len(self.items) - 1:
            left_child = current * 2
            right_child = current * 2 + 1
            max_node = current

            if left_child < len(self.items) and self.items[left_child] > self.items[max_node]:
                max_node = left_child
            if right_child < len(self.items) and self.items[right_child] > self.items[max_node]:
                max_node = right_child

            if max_node == current:
                break
            self.items[current], self.items[max_node] = self.items[max_node], self.items[current]
            current = max_node

        return del_element  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]
