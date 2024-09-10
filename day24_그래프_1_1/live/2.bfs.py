# page31. 연습문제2
import sys
sys.stdin = open("graph.txt", "r")

'''
숫자 N을 * 2 / - 1 / + 1을 할 수 있다.
M으로 만드는 최소 횟수는?
-> BFS로 풀기(퍼져나가면서 체크하는 유형)

DFS vs BFS
1. 둘 다 되는 문제가 더 많음
- ~로 갈 수 있는지 구하여라

BFS : 지하철 노선도, 최소 거리

'''
def bfs(node):
    q = [node]      # 선입선출

    while q:        # q에 저장되는 데이터 : 다음에 처리할 데이터(후보군)
        now = q.pop(0)      # 가장 앞에 있는 데이터 출력

        print(now, end=' ')  # 현재 노드 출력

        # 현재 정점에서 인접한 정점들을 확인
        for next_node in graph[now]:
            # 이미 방문한 정점이면 통과
            if visited[next_node]:
                continue

            # 방문 처리
            visited[next_node] = 1
            q.append(next_node)     # 후보군에 추가가

'''
그래프를 만드는 코드는 FS, BFS 동일
핵심은 무슨 노드를 먼저 탐색할 것인가
- 갈 수 있으면 끝까지 가자 : DFS
- 특정 정점을 기준으로 퍼져나가면서 확인하자 : BFS
'''
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1] = 1
bfs(1)
