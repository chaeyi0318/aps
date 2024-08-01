import sys
sys.stdin = open('1966_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    length = len(arr)

    for i in range(length - 1):
        min_idx = i

        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    print(f'#{tc}', end=' ')
    print(*arr)