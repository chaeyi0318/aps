'''
7
3 5 1 2 7 4 -5
'''


class Node:
    def __init__(self, key):  # 연결리스트 형태로 만들거라 이 형태 좌 - data - 우
        self.key = key
        self.left = None
        self.right = None


# BST 구현 부분
class BinarySearchTree:
    def __init__(self):  # 관리할 데이터는 최상위 root
        self.root = None

        # 삽입

    def insert(self, key):
        if self.root is None:  # 아무것도 없을 경우 걍 삽입
            self.root = Node(key)
        else:  # 값이 있다면 자리를 찾아서 삽입
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:  # 작으면 왼쪽
            if node.left is None:  # 가능하면 왼쪽에 삽입
                node.left = Node(key)
            else:  # 왼쪽에 데이터가 있는 경우
                self._insert(node.left, key)  # 또 내려가서 탐색 (재귀)
        else:  # 오른쪽
            if node.right is None:  # 가능하면 오른쪽에 삽입
                node.right = Node(key)
            else:  # 오른쪽에 데이터가 있는 경우
                self._insert(node.right, key)  # 재귀로 다시 탐색

    def search(self, key):
        return self._search(self.root, key)

    # 탐색
    # key = target
    def _search(self, node, key):
        if node is None or node.key == key:  # 탐색하고자 하는 노드가 없거나 찾은 경우 노드 리턴
            return node
        if key < node.key:  # 작은 경우 좌 탐색
            return self._search(node.left, key)
        else:  # 큰 경우 우 탐색
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)


N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
