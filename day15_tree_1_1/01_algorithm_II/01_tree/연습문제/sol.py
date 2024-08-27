import sys

sys.stdin = open('input.txt')

# 전위 순회 (본인 - 왼쪽 - 오른쪽)
def preorder(node):
    if node == 0:
        return
    print(node, end=' ')

    preorder(left[node])
    preorder(right[node])
    # 중위, 후위는 print 위치만 바뀜
    # preorder(left[node])
    # print(node, end=' ')
    # preorder(right[node])

    # 후위
    # preorder(left[node])
    # print(node, end=' ')
    # preorder(right[node])


# left, right를 쓰는 버전
# 단, 입력이 반드시 각 노드당 최대 2번씩만 들어온다고 가정한 코드
N = int(input())  # 정점의 개수
arr = list(map(int, input().split()))

left = [0] * (N + 1)  # 왼쪽 자식 번호를 저장할 리스트
#  ex) left[3] = 2 ==> 3번 부모의 왼쪽 자식은 2다.
right = [0] * (N + 1)  # 오른쪽 자식 번호를 저장할 리스트

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i + 1]

    # 왼쪽 자식이 없다면 왼쪽에 삽입
    if left[parent] == 0:
        left[parent] = child
    # 오른쪽 자식이 없다면 오른쪽에 삽입
    else:
        right[parent] = child

# print(left)
# print(right)

root = 1    # 시작점은 1로 가정
preorder(root)

#### 코테 때는 인접리스트 활용