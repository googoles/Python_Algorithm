import functools
import sys

sys.setrecursionlimit(10**6)

preorder_list = []
postorder_list = []

class Tree:
    def __init__(self, x,y,index):
        self.x = x
        self.y = y
        self.index = index
        self.left = self.right = None

def preorder(node):
    preorder_list.append(node.index)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    postorder_list.append(node.index)

def compare(info1, info2):

    if info1[1] != info2[1]:
        return info2[1] - info1[1]
    else:
        return info1[0] - info2[0]


def solution(nodeinfo):
    answer = []
    nodeinfo_with_idx = [info + [idx + 1] for idx, info in enumerate(nodeinfo)]
    nodeinfo_with_idx.sort(key = functools.cmp_to_key(compare))

    root_node = None

    for node in nodeinfo_with_idx:
        if not root_node:
            root_node = Tree(node[0], node[1], node[2])
        else:
            x = node[0]
            current_node = root_node
            while True:
                if x < current_node.x:
                    if current_node.left:
                        current_node = current_node.left
                        continue
                    else:
                        current_node.left = Tree(node[0],node[1],node[2])
                        break
                if x > current_node.x:
                    if current_node.right:
                        current_node = current_node.right
                        continue
                    else:
                        current_node.right = Tree(node[0],node[1],node[2])
                        break
                break
    preorder(root_node)
    postorder(root_node)
    answer.append(preorder_list)
    answer.append(postorder_list)
    return answer


