import sys

sys.stdin = open('input.txt')

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # index 에러 방지를 위해 + 1
    visited = [0] * (N * N + 1)

    # 전체를 순회하며 상하좌우에 나보다 1이 크다면 visited 체크
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]

                if 0 < ny <= N or 0 < nx <= N:
                    continue

                if arr[ny][nx] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    # 이미 체크된 순간 다른 방향은 볼 필요가 없음 => 왜? => 동일한 숫자가 없기 때문
                    break

    # cnt : 하나씩 체크 / max_cnt : 정답 / start : 시작 위치
    cnt = max_cnt = start = 0

    for i in range(N * N - 1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0
    print(start, max_cnt + 1)