import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    end = -1

    for item in arr:
        if item[0] >= end:
            cnt += 1
            end = item[1]

    print(f'#{t}', cnt)