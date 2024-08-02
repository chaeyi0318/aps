import sys

sys.stdin = open('1989_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = input()
    revers = list(N)

    for i in range(len(revers) // 2):
        revers[i], revers[len(revers) - i - 1] = revers[len(revers) - i - 1], revers[i]

    tmp = ''.join(revers)

    result = 1 if tmp == N else 0

    print(f'#{tc} {result}')