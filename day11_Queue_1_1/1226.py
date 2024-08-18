dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def dfs2(i, j, N):
    maze[i][j] = 1

    if maze[i][j] == 3:
        return 1
    else:
        for dx, dy in dxy:
            nx, ny = i + dx, j + dy

            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                if dfs2(nx, ny, N):
                    return 1
        return 0


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1, -1


for _ in range(10):
    T = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    start_i, start_j = find_start(16)

    visited = [[0] * 16 for _ in range(16)]

    print(f'#{T} {dfs2(start_i, start_j, 16)}')
