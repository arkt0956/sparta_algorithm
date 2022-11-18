class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index-1)
        new_node.next = node.next
        node.next = new_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        new_node = self.get_node(index-1)
        new_node.next = new_node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(0).data) # -> 5를 들고 있는 노드를 반환해야 합니다!