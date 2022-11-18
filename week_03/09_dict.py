# class Dict:
#     def __init__(self):
#         self.items = [None] * 8
#
#     def put(self, key: int, value: int) -> None:
#         length: int = len(self.items)
#         index = hash(key) % length
#         self.items[index] = value
#
#     def get(self, key):
#         return self.items[hash(key)%8]
#
#
#
# my_dict = Dict()
# my_dict.put("test", 3)
# print(my_dict.get("test"))  # 3이 반환되어야 합니다!

class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        length = len(self.items)
        index = hash(key) % length
        self.items[index].add(key, value)

    def get(self, key):
        length = len(self.items)
        index = hash(key) % length
        return self.items[index].get(key)
