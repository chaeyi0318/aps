import sys

sys.stdin = open('input.txt')


def binary_num(n):
    result = ''
    cnt = 0

    while n > 0:
        if cnt >= 13:
            return 'overflow'

        n *= 2

        if n >= 1:
            result += '1'
            n -= 1
        elif n < 1:
            result += '0'

        cnt += 1

    return result


T = int(input())

for t in range(1, T + 1):
    N = float(input())

    print(f'#{t}', binary_num(N))
