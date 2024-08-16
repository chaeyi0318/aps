'''
2
2
1 3
2 5
5
1
2
3
4
5
2
1 3
2 5
5
1
2
3
4
5

'''

T = int(input())

for t in range(1, T + 1):
    N = int(input())        # 노선 수
    cnt = [0] * 5001    # 정류장

    # N개의 노선 정보를 모두 읽어놓고 처리 or 읽을 때마다 처리
    for n in range(N):
        Ai, Bi = map(int, input().split())

        for i in range(Ai, Bi + 1):     # 1 <= Ai <= Bi <= 5000
            cnt[i] += 1

    P = int(input())    # 노선을 출력할 수
    busstop = [int(input()) for _ in range(P)]      # 숫자를 모두 읽고 처리

    print(f'#{t}', end=' ')

    for j in busstop:
        print(cnt[j], end=' ')
    print()

    # print(f'#{t}', end=' ')
    #
    # for _ in range(P):
    #     C = int(input())
    #
    #     print(cnt[C], end=' ')