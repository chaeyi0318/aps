def check_bingo(tmp):
    # 가로 탐색
    for i in range(5):
        if board[i] == [0] * 5:
            tmp += 1
    # 세로 탐색
    for i in range(5):
        if all(board[j][i] == 0 for j in range(5)):
            tmp += 1

    # 좌 - 우 대각선 탐색
    if all(board[i][i] == 0 for i in range(5)):
        tmp += 1

    # 우 - 좌 대각선 탐색
    if all(board[i][4 - i] == 0 for i in range(5)):
        tmp += 1

    return tmp


board = [list(map(int, input().split())) for _ in range(5)]
bingo = []

for _ in range(5):
    bingo += list(map(int, input().split()))

tmp = 0
cnt = 0

for x in range(25):
    for i in range(5):
        for j in range(5):
            if bingo[x] == board[i][j]:
                board[i][j] = 0
                cnt += 1

    if cnt >= 12:
        result = check_bingo(tmp)
        if result >= 3:
            print(x + 1)
            break
