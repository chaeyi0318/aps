'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''


def bfs(start, V):  # 1, 마지막 정점 V
    # 준비
    visited = [0] * (V + 1)  # visited 생성
    q = []  # 큐 생성
    q.append(start)  # 시작점 인큐
    visited[start] = 1  # 시작점 방문(인큐됨) 표시

    # 탐색
    while q:  # 탐색할 정점이 남아있으면
        t = q.pop(0)  # 디큐
        print(t)  # 처리
        for w in adj_l[t]: # t에 인접이고, 인큐된적이 없으면
            if visited[w] == 0:
                q.append(w) # 인큐하고 인큐 표시
                visited[w] = 1



V, E = map(int, input().split())  # V = 마지막 정점 번호, E = 간선 수
arr = list(map(int, input().split()))

adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]  # 한 쌍씩 읽음
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)  # 방향이 없는 경우
print(adj_l)
bfs(1, V)  # 1번부터 시작하고 마지막 정점 V
