### 이진 탐색 트리 

- 최대 두 개의 자식 노드를 가지는 트리 형태의 자료구조
- 값을 저장하기 위한 용도가 아닌, 효율적인 탐색 혹은 정렬을 위해 사용
- 시간복잡도 O(log n)

### 구현 방법

1. 배열이나 주어진 값들이 들어온다.
2. 주어진 값을 기준으로 값이 크면 우측, 값이 작으면 좌측
3. 해당 과정을 반복 시킨다.

위와 같은 구조를 가지려면 Node가 있어야하고, Node는 data와 tails를 가지고 있어야한다.
그렇기 때문에 class 로 Node를 만들어 줄 때 초기 선언을 해주어야한다. 
``` python
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
```

이후 Node를 가지고 계속 이어 나갈수 있도록 이진 탐색 트리를 구현해야 한다,
``` python
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
```
비어있는 루트를 만들어 주고 난 뒤, 값을 붙여주는 함수를 구현해야한다.
데이터를 붙이는(?) 함수와, 데이터를 배치하는(?) 함수를 구현한다. ( 이해한대로,, )

``` python
class BinarySearchTree(object):
    ...
    # 데이터를 붙이는(?) 함수
    def insert(self, data):
        self.root = self.insertValue(self.root, data)
        return self.root is not None

    # 데이터를 배치하는(?) 함수
    def insertValue(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self.insertValue(node.left, data)
            else:
                node.right = self.insertValue(node.right, data)
        return node
```
이후 값의 유무를 존재하는 함수들을 구현한다. 값을 찾는 함수를 호출하는 함수와 값을 실제 서치하는 함수를 호출한다.
``` python
class BinarySearchTree(object):
    ...
    # 값을 찾는 함수를 호출하는 함수
    def find(self, key):
        return self.findValue(self.root, key)

    def findValue(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self.findValue(root.left, key)
        else:
            return self.findValue(root.right, key)
```
insertValue 나 findValue 부분을 보게 되면 자신의 key 값이 root보다 작으면 좌측 노드를 root로 올리고, 크면 우측 노드를 root 로 올려서 값을 탐색할 수 있도록 한다. 

테스트는 아래와 같이 입력하면 동작한다.

```python
if __name__ == "__main__":
    array = [40,20,10,15,29,55,99,31,46,77]

    bst = BinarySearchTree()
    for x in array:
        bst.insert(x) # 입력 과정

    # 찾는 과정
    print(bst.find(10)) # True
    print(bst.find(70)) # False 
```

### 삭제부분은 아직 제대로 동작시켜보지 못해서 작성하지 않았다.