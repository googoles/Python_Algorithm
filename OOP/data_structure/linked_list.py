# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
'''
node1 = Node(1)
node2 = Node(2)
node1.next= node2
head = node1
'''


# def add(data):
#     node = head
#     while node.next:
#         node = node.next
#     node.next = Node(data)
#
# node1 = Node(1)
# head = node1
# for index in range(2,10):
#     add(index)
# print(Node(1))

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)


def desc(self):
    node = self.head
    while node:
        print(node.data)
        node = node.next

linkedlist1 = NodeMgmt(0)
for data in range(1,10):
    linkedlist1.add(data)
print(linkedlist1)
