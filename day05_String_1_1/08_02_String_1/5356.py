import sys
sys.stdin = open('5356_input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = [input() for _ in range(5)]

    print(f'#{tc}',end=' ')

    for i in range(15):
        for j in range(5):
            if i < len(arr[j]):
                print(arr[j][i], end='')
    print()
