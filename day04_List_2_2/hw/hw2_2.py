import sys

sys.stdin = open('input.txt')

T = 10
dx = [-1, 0, 0]
dy = [0, -1, 1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    i_idx = 99
    j_idx = 0  # 열
    print(f'{tc}번째 -------------------')
    for j in range(100):
        if arr[len(arr) - 1][j] == 2:
            j_idx = j

        # i = int(input()) 행
        # j = int(input()) 열
        #
        # for x in range(4):
        #     point_i = i + di[x]
        #     point_j = j + dj[x]
        #     print(arr[point_i][point_j])

    while i_idx != 0:
        for x in range(3):
            point_i = i_idx + dx[x]
            point_j = j_idx + dy[x]

            if 0 <= point_i <= 99 and 0 <= point_j <= 99:
                if arr[point_i][point_j] == 1:
                    i_idx = point_i
                    j_idx = point_j
                    print(arr[point_i][point_j])
                    print('point index : ', point_i, point_j)
                    print('i, j index : ', i_idx, j_idx)
                    print('주변 값 ', arr[point_i][point_j])

    # print('-' * 10)

    # 2 위치 arr[99][idx]에서 1 찾아서 위로 올라가기
    # 지나온 곳 0으로 바꾸기
    # visited 지나온걸 확인한느 변수 만들기
    # visited = [[0] * 100 for _ in range(100)]
    # print(idx)
