import sys

sys.stdin = open('ladder_input.txt')

dxy = [[-1, 0], [0, -1], [0, 1]]

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    start_i = 99
    start_j = 0

    for j in range(len(arr)):
        if arr[99][j] == 2:
            start_j = j
            break

    while start_i != 0:
        for x in range(len(dxy)):
            point_i = start_i + dxy[x][0]
            point_j = start_j + dxy[x][1]

            if 0 <= point_i < len(arr) and 0 <= point_j < len(arr[0]) and arr[point_i][point_j] != 0:
                arr[point_i][point_j] = 0
                start_i, start_j = point_i, point_j

    print(f'#{t} {start_j}')
