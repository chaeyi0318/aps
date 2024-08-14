import sys
from collections import deque

sys.stdin = open('5097_input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    num_deque = deque(map(int, input().split()), maxlen=N)

    for m in range(M):
        tmp = num_deque.popleft()
        num_deque.append(tmp)

    print(f'#{t}', num_deque[0])

