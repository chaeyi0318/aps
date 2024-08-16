dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]


def f(N):
    for i in range(N):
        for j in range(N):
            for k in range(4):
                cnt = 0
                nx, ny = i, j  # 돌인지 확인할 위치

                while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                    cnt += 1

                    if cnt == 5:
                        return 'YES'
                    nx += dx[k]
                    ny += dy[k]

    return 'NO'  # 모든 자리 i, j에서 모든 방향 k에 대해 실패할 때


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    result = f(N)
    print(f'#{t} {result}')
