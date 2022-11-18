

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.count = 1

    def append(self, value):
        cur = self.head
        while cur != self.tail:
            cur = cur.next
        cur.next = Node(value)
        self.tail = cur.next
        self.count += 1

    def get_kth_node_from_last(self, k: int) -> Node:
        current = self.head
        while self.count - k > 0:
            current = current.next
            k += 1
        return current


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
print(linked_list.get_kth_node_from_last(4).data)