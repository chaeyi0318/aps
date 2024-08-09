import sys

sys.stdin = open('11092_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = len(arr)
    max_idx = 0

    for i in range(len(arr) - 1):
        if min_idx < arr[i]:
            min_idx = i