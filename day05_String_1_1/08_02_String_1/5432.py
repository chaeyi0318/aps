# 레이저 = 무조건 ()
# 쇠막대기 = (((())))
import sys
sys.stdin = open('5432_input.txt')
T = int(input())

for tc in range(1, T + 1):
    li = list(input())
    print('  '.join(li))

    # tmp = ''
    # tmp += li.pop()