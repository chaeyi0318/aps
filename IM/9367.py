import sys

sys.stdin = open('9367_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt, max_cnt = 1, 1

    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            cnt += 1

            if cnt > max_cnt:
                max_cnt = cnt
    print(f'#{t}', max_cnt)
