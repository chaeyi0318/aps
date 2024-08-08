import sys

sys.stdin = open('sample_input.txt')

# 재귀
def dfs2(i, j, N):
    visited[i][j] = 1
    if maze[i][j] == 3:
        return 1
    else:
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                if dfs2(ni, nj, N):
                    return 1
        return 0


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    start_i, start_j = find_start(N)
    # 방문한 칸을 표시할 visited
    visited = [[0] * N for _ in range(N)]  # dfs2 용
    print(f'#{t} {dfs2(start_i, start_j, N)}')
