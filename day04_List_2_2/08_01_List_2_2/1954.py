import sys

sys.stdin = open('1954_input.txt')

T = int(input())

dxy = [[]]

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    num = 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = num
            num += 1

    print(arr)