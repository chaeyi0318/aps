N_pole = 1      # N극
S_pole = 2      # S극

T = 10

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for j in range(100):        # 열 우선 순회
        np = 0

        for i in range(100):
            if arr[i][j] == N_pole:
                np = 1
            elif arr[i][j] == S_pole and np == 1:
                cnt += 1
                np = 0

    print(f'#{t} {cnt}')