import sys

sys.stdin = open('1219_input.txt')

for t in range(10):
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))

    print(arr)