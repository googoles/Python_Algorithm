# class Stack(list): # List 를 활용한 Stack 구현
#
#     def __init__(self):
#         self.stack = []
#
#     def push(self,data):
#         self.stack.append(data)
#
#     def pop(self):
#         if self.is_empty():
#             return -1
#         return self.stack.pop()
#
#     def peek(self):
#         return self.stack[-1]
#
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         return False
#
# if __name__=="__main__":
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     print(s.peek())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())
#     print(s.pop())

# Singly Linked list을 활용한 Stack 구현

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        return data





# test1 = ['a','b','c']
#
# # print(test1.index('b'))
#
# def find(arr,ch):
#     i = -1
#     for c in arr:
#         i += 1
#         if ch == c:
#             return i
#     else:
#         return -1
#
# print(find(test1,'b'))
# print(find(test1,'d'))