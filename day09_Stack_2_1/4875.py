import sys

sys.stdin = open('4875_input.txt')

T = int(input())


def dfs(i, j, N):
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited[i][j] = 1

    if maze[i][j] == 3:
        return 1

    for x in range(len(dxy)):
        point_x = i + dxy[x][0]
        point_y = j + dxy[x][1]

        if 0 <= point_x < N and 0 <= point_y < N and maze[point_x][point_y] != 1 and visited[point_x][point_y] == 0:
            if dfs(point_x, point_y, N):
                return 1
    return 0


for t in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    start_x, start_y = 0, 0

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:
                start_x = i
                start_y = j
                break

    print(f'#{t}', dfs(start_x, start_y, N))

    # print(start_x, start_y)

# T = int(input())
#
# def dfs(i, j, N):
#     dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
#     for x in range(len(dxy)):
#         point_x = i + dxy[x][0]
#         point_y = j + dxy[x][1]
#
#         if 0 <= point_x < len(maze) and 0 <= point_y < len(maze):
#             print(maze[point_x][point_y])
#
#
# def find_start(maze):
#     for i in range(len(maze)):
#         for j in range(len(maze[i])):
#             if maze[i][j] == 2:
#                 return i, j
#
# for t in range(1, T + 1):
#     N = int(input())
#     maze = [list(map(int, input())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#
#     start_i, start_j = find_start(maze)
#
#     print(dfs)
#
