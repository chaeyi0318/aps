import sys

sys.stdin = open('input.txt')
'''
2   T
5 2 2   N, M, B = 배열크기, 파리채 크기, 방사능 파리가 있는 칸 수
2 2     파리 위치
3 5     파리 위치
1 3 3 6 7   배열
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''
T = int(input())

dxy = [[-1, -1], [-1, 1], [1, -1], [1, 1]]      # 대각선 탐색
#       좌상        우상      좌하      우하

for t in range(1, T + 1):
    N, M, B = map(int, input().split())
    b_idx_arr = [list(map(int, input().split())) for _ in range(B)]
    b_idx_arr = [[x - 1, y - 1] for x, y in b_idx_arr]
    # board = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    print(board)

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            cnt = 0
            visited = [[False] * N for _ in range(N)]

            for mx in range(M):
                for my in range(M):
                    if not visited[i + mx][j + my]:
                        cnt += board[i + mx][j + my]
                        visited[i + mx][j + my] = True

                    for b_i, b_j in b_idx_arr:
                        if i + mx == b_i and j + my == b_j:
                            for dx, dy in dxy:
                                nx, ny = (i + mx) + dx, (j + my) + dy
                                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                                    cnt += board[nx][ny]
                                    visited[nx][ny] = True

            if cnt > result:
                result = cnt
    print(result)