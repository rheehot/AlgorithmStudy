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
        
    def delete(self, key):
        self.root, deleted = self.deleteValue(self.root, key)
        return deleted

    def deleteValue(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = child, node.right
            while child.left is not None:
                parent, child = child, child.left
            child.left = node.left
            if parent != node:
                parent.left = child.right
                child.right = node.right
            elif node.left or node.right:
                node = node.loft or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self.deleteValue(node.left, key)
        else:
            node.right, deleted = self.deleteValue(node.right, key)
        return node, deleted

array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# 여기 아래부터 제대로 실행은 되지 않지만, 찾기는 정상적으로 가능
# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False
            
