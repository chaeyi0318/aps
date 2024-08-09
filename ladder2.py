import sys

sys.stdin = open('ladder2_input.txt')

dxy = [[0, 1], [0, -1], [1, 0]]

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for j in range(len(arr)):
        if arr[0][j] == 1:
            start_i = j

            while start_i != 99:
                for x in range(len(dxy)):
                    point_i = start_i + dxy[x][0]