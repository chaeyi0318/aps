def f(i, j, bw, N):
    board[i][j] = bw  # 지정된 돌 놓기
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
        nx, ny = i + dx, j + dy
        tmp = []

        while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == op[bw]:
            tmp.append((nx, ny))
            nx, ny = nx + dx, ny + dy
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == bw:
            for p, q in tmp:
                board[p][q] = bw


# 1 : 흑 / 2 : 백
B = 1
W = 2
op = [0, 2, 1]

T = int(input())

dxy = [[]]

for t in range(1, T + 1):
    N, M = map(int, input().split())
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]

    # 중심부 돌 배치
    # WB
    # BW 로 배치

    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    # 돌 놓기
    for col, row, color in play:  # 입력순으로 변수 지정
        f(row - 1, col - 1, color, N)  # 돌 넣고 뒤집는 함수
    bcnt, wcnt = 0, 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1

    print(f'#{t} {bcnt} {wcnt}')
    # 내 풀이
    # N, M = map(int, input().split())  # N * N / M : 돌을 놓는 횟수
    # arr = [[0] * N for _ in range(N)]
    #
    # for i in range(N // 2, N // 2 + 1):
    #     for j in range(i):
    #         if i % 2 == 0:
    #             arr[i][j] = 2
    #         else:
    #             arr[i][j] = 1
    #
    # for _ in range(M):
    #     i, j, color = map(int, input().split())
    #     arr[i - 1][j - 1] = color  # idx는 0부터 시작이라 - 1 해주기
    #
    # print(arr)
