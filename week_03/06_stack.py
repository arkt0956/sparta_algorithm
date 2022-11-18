class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    # pop 기능 구현
    def pop(self) -> Node:
        if self.head is None:
            return
        else:
            pop_node = self.head
            self.head = self.head.next
        return pop_node

    def peek(self) -> Node:
        if self.head is None:
            print("Empty Stack")
        return self.head

    # isEmpty 기능 구현
    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False


stack = Stack()
print(stack.is_empty())
stack.push(3)
print(stack.peek().data)
stack.push(4)
print(stack.peek().data)
print(stack.pop().data)
print(stack.peek().data)
print(stack.is_empty())
