import sys
from collections import deque
sys.stdin = open('practice_input.txt')


dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_road_move_time(road, n, m):
    # 도착 지점 n - 1, m - 1
    queue = deque([0, 0])

    # visited 겸 복사 (이동 시간을 저장하는 리스트)
    distance = [[-1] * m for _ in range(n)]
    # 방문표시
    distance[0][0] = 0

    print(queue.popleft())

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 범위 검사하고
            if 0 > nx or nx >= n or 0 > ny or ny >= m: continue
            # 갈 수 있는 길인지 확인
            if road[nx][ny] == 0: continue
            # 방문 확인
            if distance[nx][ny] != -1: continue
            # 조건 통과하면 append
            queue.append((nx, ny))
            # distance 변수에 현재 위치까지 오는데 걸리는 시간 + 1 저장
            distance[nx][ny] = distance[x][y] + 1

            if nx == n - 1 and ny == m - 1:
                return distance[nx][ny]
    # 목적지 못 찾음
    return -1


n, m = map(int, input().split())
road = [list(map(int, input())) for _ in range(n)]
print(road)
result = get_road_move_time(road, n, m)
print(result)
