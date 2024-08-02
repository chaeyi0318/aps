import sys

sys.stdin = open('19606_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    idx = len(arr) - 1

    for i in range(len(arr)):
        result += arr[i][i]
        result += arr[i][idx]
        idx -= 1
        # result += arr[i][i]
        # arr[i][i] = 0
    print(result)
    print('-' * 10)
    # print(result)