import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())        # 컨테이너 , 트럭 수
    w = list(map(int, input().split()))     # 화물 무게
    t = list(map(int, input().split()))     # 트럭 적재용량
    result = 0

    w.sort(reverse=True)
    t.sort(reverse=True)

    num = 0

    for i in range(len(w)):
        while num < len(t):
            if w[i] <= t[num]:
                result += w[i]
                num += 1
                break
            else:
                break

    print(f'#{tc}', result)