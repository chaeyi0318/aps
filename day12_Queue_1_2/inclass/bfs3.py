T = int(input())


def bfs(start_i, start_j, N):
    # 준비
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q = []  # 큐 생성
    q.append([start_i, start_j])  # 시작점 인큐
    visited[start_i][start_j] = 1  # 시작점 인큐 표시

    # 탐색
    while q:
        ti, tj = q.pop(0)  # 디큐
        if maze[ti][tj] == 3:  # visited(t)
            return visited[ti][tj] - 1 - 1  # 경로의 빈칸 수
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 인접이고 벽이 아니면서, 미로를 벗어나지 않는 경우
            wi, wj = ti + di, tj + dj

            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])  # 인큐
                visited[wi][wj] = visited[ti][tj] + 1  # 인큐 표시

    return 0


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start_i, start_j = find_start(N)
    ans = bfs(start_i, start_j, N)

    print(ans)
