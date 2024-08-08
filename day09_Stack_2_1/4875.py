import sys

sys.stdin = open('4875_input.txt')

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())

def find_start(maze):



for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    start_i, start_j = find_start(maze)

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:
                start[0] = i
                start[1] = j

    stack = [start]

    # while stack:
    for x in range(len(dxy)):
        point_x = start[0] + dxy[x][0]
        point_y = start[1] + dxy[x][1]

        if 0 <= point_x < len(maze) and 0 <= point_y < len(maze):
            print(maze[point_x][point_y])

    print()

            # stack.append([point_x, point_y])

