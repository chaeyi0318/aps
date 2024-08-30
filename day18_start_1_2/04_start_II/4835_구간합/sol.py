import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    min_value = 0
    max_value = 0

    for i in range(len(arr) - M + 1):
        tmp = 0

        for j in range(i, i + M):
            tmp += arr[j]

        if tmp > max_value:
            max_value = tmp

        if min_value == 0:
            min_value = tmp
        elif tmp < min_value:
            min_value = tmp

    print(f'#{t}', max_value - min_value)
