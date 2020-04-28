# import random
# a_count = 0; b_count = 0; c_count = 0; Z = 0; P = 3; z = 0
# for _ in range(10):
#     i = random.randint(1,3)
#     if i == 1:
#         a_count += 1
#     if i == 2:
#         Z = z + 1
#     if z == P:
#         a_count += 1
#         z = 0
#     else:
#         b_count += 1
#     if i == 3:
#         c_count += 1
# print(a_count,b_count,c_count)

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left, self.right = None, None
#
# class NodeMgmt:
#     def __init__(self, head):
#         self.head = head
#
#     def insert(self, value):
#         self.current_node = self.head
#         while True:
#             if value < self.current_node.value:
#                 if self.current_node.left != None:
#                     self.current_node = self.current_node.left
#                 else:
#                     self.current_node.left = Node(value)
#                     break
#             else:
#                 if self.current_node.right != None:
#                     self.current_node = self.current_node.right
#                 else:
#                     self.current_node.right = Node(value)
#                     break
#
# head = Node(1)
# binary_tree = NodeMgmt(head)
#
# binary_tree.insert(2)

class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class NodeMgmt:
    def __init__(self, node):
        self.head = node

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
