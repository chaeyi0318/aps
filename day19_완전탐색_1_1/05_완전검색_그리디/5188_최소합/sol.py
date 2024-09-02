import sys

sys.stdin = open('input.txt')

dxy = [[0, 1], [1, 0]]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 9999999