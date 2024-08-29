from collections import deque

T = int(input())  # 테스트 케이스

for _ in range(T):
    N, M = map(int, input().split())  # N : 문서 개수 / M : 현재 궁금한 문서의 idx

    tmp = list(map(int, input().split()))
    queue = deque((i, tmp[i]) for i in range(N))        # (인덱스, 중요도)
    cnt = 0
    print(max(queue))
    # while True:
    #     if queue.popleft()[1] < max(queue[1])
    # print(queue.popleft())

    # deque([(0, 5)])
    # deque([(0, 1), (1, 2), (2, 3), (3, 4)])
    # deque([(0, 1), (1, 1), (2, 9), (3, 1), (4, 1), (5, 1)])
