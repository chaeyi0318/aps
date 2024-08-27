import sys

sys.stdin = open('input.txt')


def search(node):   # node == N
    global cnt      # 함수 밖에 선언해둔 cnt

    if node != 0:   # node가 0인 경우는 없음
        cnt += 1        # cnt += 1
        search(graph[node][0])      # 왼쪽 탐색
        search(graph[node][1])      # 오른쪽 탐색

    return cnt      # cnt return


T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())  # E : 간선 / N : N을 루트로 하는 서브 트리에 속한 노드의 개수를 찾을 때
    arr = list(map(int, input().split()))  # 부모 - 자식 노드 번호 쌍

    graph = [[0, 0] for _ in range(E + 2)]      # 노드번호는 1번부터 E + 1까지 존재하기 때문에 + 2

    for i in range(len(arr) // 2):      # arr에서 부모-자식 노드 쌍은 두 개의 요소로 구성되기 때문에, 전체 쌍의 수는 리스트 길이의 절반
        p = arr[i * 2]      # 부모
        c = arr[i * 2 + 1]  # 자식

        if graph[p][0] == 0:    # 부모의 왼쪽에 자식이 아직 입력이 안된 경우
            graph[p][0] = c
        else:                   # 부모의 오른쪽에 자식이 아직 입력이 안된 경우
            graph[p][1] = c

    cnt = 0     # 노드의 개수를 찾을 변수
    result = search(N)      # search 함수랑 N(노드)

    print(f'#{t}', result)
