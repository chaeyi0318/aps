import sys
sys.stdin = open('input.txt')

# 1 : 1 : 2 비율
T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    print(arr)
