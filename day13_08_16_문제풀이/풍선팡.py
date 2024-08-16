T = int(input())

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 행, 열
    arr = [list(map(int, input().split())) for _ in range(N)]  # 풍선
    result = 0

    # 꽃가루 최대 합계 구하기
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cnt = arr[i][j]  # 터진 풍선에서 나오는 꽃가루 개수

            for k in range(len(dxy)):  # 탐색
                for x in range(1, arr[i][j] + 1):  # 주변 방향으로 추가로 터지는 풍선과의 거리
                    dx = i + (dxy[k][0] * x)
                    dy = j + (dxy[k][1] * x)

                    if 0 <= dx < N and 0 <= dy < M:
                        cnt += arr[dx][dy]

            if result < cnt:
                result = cnt

    print(f'#{t}', result)
