import sys
sys.stdin = open('10760_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)