import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print(arr)

    for i in range(N):
        for j in range(N):
            pass
