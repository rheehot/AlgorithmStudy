# -*- coding: utf-8 -*-
import sys

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertValue(self.root, data)
        return self.root is not None

    def insertValue(self, node, data):
        if node is None:
            node = Node(data)
        else: 
            if data <= node.data:
                node.left = self.insertValue(node.left, data)
            else:
                node.right = self.insertValue(node.right, data)
        return node

    def find(self, key):
        return self.findValue(self.root, key)

    def findValue(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.findValue(root.left, key)
        else:
            return self.findValue(root.right, key)
        
    

# 입력값
q = list(map(int,sys.stdin.readline().split()))
# 이중 리스트로 입력을 받을까?
# 4 5 1 
# (노드의 수, 반복 횟수, 탐색을 시작할 정점의 수? 1 부터구만..)
# 모두 양방향이니까, 입력받은 값의 양쪽을 표현할 수 있어야하고 
# 이동 가능한 노드
node = list()
for i in range(q[1]):
    node.append(list(map(int,sys.stdin.readline().split())))
print(node)