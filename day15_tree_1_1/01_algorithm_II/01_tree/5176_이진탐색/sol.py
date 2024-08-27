import sys

sys.stdin = open('input.txt')


def binary_tree(x):     # x = 노드 번호
    global n    # 해당 노드에 넣을 숫자

    if x <= N:      # 인덱스를 넘으면 안되니까 조건문
        binary_tree(x * 2)      # 트리의 왼쪽 노드 : 왼쪽 노드는 루트 * 2임, 재귀 -> x가 N보다 작거나 같을 경우로 ㄱㄱ,
        tree[x] = n             # 트리의 x번째에 n 넣기

        n += 1                  # 숫자 넣었으니까 n + 1 하기
        binary_tree(x * 2 + 1)      # 트리의 오른쪽 노드 : 오른쪽는 루트 * 2 + 1임. 재귀 ㄱㄱ


T = int(input())

for t in range(1, T + 1):
    N = int(input())        # N / 2번 노드 구할 때 사용

    tree = [0] * (N + 1)  # 0번 인덱스 사용 안함

    n = 1  # 노드에 넣을 숫자

    binary_tree(1)      # 노드 인덱스

    print(f'#{t}', tree[1], tree[N // 2])
