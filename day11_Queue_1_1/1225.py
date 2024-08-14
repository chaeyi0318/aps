import sys
from collections import deque

sys.stdin = open('1225_input.txt')

for _ in range(10):
    t = input()
    num_deque = deque(map(int, input().split()))
    num = 1  # 1 ~ 5

    while True:
        if num > 5:  # 감소할 숫자인 num이 5보다 커지면 1로 다시 재할당
            num = 1

        tmp = num_deque.popleft() - num  # num_deque의 왼쪽 원소를 tmp에 할당

        if tmp <= 0:  # tmp가 0이거나 0보다 작은 경우 0을 append하고 break
            num_deque.append(0)
            break
        else:
            num_deque.append(tmp)  # 아닌 경우 num_deque에 append(tmp) 하고 사이클 돌릴 num + 1
            num += 1

    print(f'#{t}', *num_deque)
