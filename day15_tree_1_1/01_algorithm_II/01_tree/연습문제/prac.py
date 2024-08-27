import sys

sys.stdin = open('input.txt')


def search(node):   # 해당 노드 정보를 토대로 왼쪽, 오른쪽 조사
    if node != 0:   # 0번 노드는 없음
        preorder.append(node)
        search(tree[node][0])   # 왼쪽 조사
        inorder.append(node)
        search(tree[node][1])   # 오른쪽 조사
        postorder.append(node)

V = int(input())  # 전체 노드 수
arr = list(map(int, input().split()))
# tree 정보를 입력할 수 있도록 하겠다.
# tree 리스트의 index 번호 -> 부모 노드의 번호
# tree[parent] 위치의 리스트의 0번째 -> 왼쪽 자식
# tree[parent] 위치의 리스트의 1번째 -> 오른쪽 자식

tree = [[0, 0] for _ in range(V + 1)]  # 0번 노드 안 쓸거니까 + 1만큼

for i in range(len(arr) // 2):  # 간선 정보
    p, c = arr[i * 2], arr[i * 2 + 1]

    if tree[p][0] == 0: # 아직 왼쪽 자식 정보 기록한 적 없다면
        tree[p][0] = c
    else:   # 왼쪽 자식 정보가 있으면
        tree[p][1] = c

preorder = []
inorder = []
postorder = []

search(1)

print(*preorder)
print(*inorder)
print(*postorder)