import sys

sys.stdin = open('input.txt')


# target = 삽입한 위치
def enqueue(target):
    # 단순히 tree에 삽입 대상을 집어 넣는게 아니라
    # 삽입 한 후에, 부모노드와 내 노드의 크기를 비교해서
    # 부모 노드의 값이 내 노드 값보다 크다면 swap
    while target // 2:
        parent = target // 2

        if tree[target] <= tree[parent]:
            tree[target], tree[parent] = tree[parent], tree[target]
        target = parent


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0]

    # tree = [0] * (N + 1)  # 해도 됨
    # 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
    last_node = 0       # 마지막 노드의 조상 노드에 저장된 정수의 합

    for item in arr:
        tree.append(item)

        last_node += 1
        enqueue(last_node)

    print(tree, last_node)