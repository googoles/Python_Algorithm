
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)  # 인덱스 번호는 1번부터
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[
                inserted_idx]
            inserted_idx = parent_idx
        return True

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
# class Heap:
#     def __init__(self,data):
#         self.heap_array = list()
#         self.heap_array.append(None)
#         self.heap_array.append(data)
#
#     def insert(self,data):
#         if len(self.heap_array) == 1:
#             self.heap_array.append(data)
#             return True
#         self.heap_array.append(data)
#         return True
# heap = Heap(1)
# heap.heap_array
# print(heap.heap_array)



# def find_same_name(name_list):
#     for index, name in enumerate(name_list):           # 반복문에 주의!
#         for index2 in range(index + 1, len(name_list)):   # 반복문에 주의!
#             if (name == name_list[index2]):
#                 del name_list[index2]
#
#     return name_list
#
# names = ['Dave', 'David', 'Anthony', 'David', 'Dave']
# print(find_same_name(names))

