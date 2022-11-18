class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value: int) -> None:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> Node:
        if self.head is None:
            return
        else:
            de_node = self.head
            self.head = self.head.next
            return de_node

    def peek(self) -> Node:
        return self.head

    def is_empty(self):
        return self.head is None
