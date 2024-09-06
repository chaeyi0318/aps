'''
시작점 : 0번 점원
끝점(기저조건) : N명의 점원을 탑에 쌓을 지 말지 고려를 완료
'''

def recur(cnt, sum_height):
    global result

    # 기저조건 가지치기 : 이미 탑의 높이가 B 이상이라면, 더 이상 확인할 필요X
    if sum_height >= B:
        # B 이상의 탑 중 가장 낮은 것이 정답!
        result = min(result, sum_height)
        return

    # 기저조건 : 모든 점원을 탑을 쌓는데 고려했는가?
    if cnt == N:
        return

    # cnt번 점원을 탑에 쌓음
    recur(cnt + 1, sum_height + heights[cnt])

    # 안쌓음
    recur(cnt + 1, sum_height)

import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = 1e9        # 점원들을 쌓은 탑 중 B에 가장 가까운 높이를 저장
    recur(0, 0)
    print(f'#{t} {result - B}')