import sys

sys.stdin = open('input.txt')

'''
시작점 : 1월 / 누적 금액 : 0원
끝점 : 12월
'''

# 접근 방법 1
# def dfs(month, sum_cost):
#     global result
#
#     # 기저조건 모두 봄?
#     if month > 12:
#         result = min(result, sum_cost)
#         return
#
#     # 1일권으로 모두 구매 (다음 재귀 : 다음 달을 확인)
#     dfs(month + 1, sum_cost + (days[month] * cost[0]))
#
#     # 1달권 구매 (다음 재귀 : 다음 달을 확인)
#     dfs(month + 1, sum_cost + cost[1])
#
#     # 3달권 구매 (다음 재귀 : 3달 후를 확인)
#     dfs(month + 3, sum_cost + cost[2])
#
#     # 1년권 구매 (다음 재귀 : 12달 후를 확인)
#     # - 사실 재귀에서 빼고, 1월에 구입한 비용이랑 비교해도 됨!
#     dfs(month + 12, sum_cost + cost[3])
#
# T = int(input())
#
# for t in range(1, T + 1):
#     cost = list(map(int, input().split()))
#     # 인덱스 1 ~ 12까지 보려고 + [0] 해줌
#     days = [0] + list(map(int, input().split()))
#     result = 1e9
#     # 시작 1월, 누적금액 0원
#     dfs(1, 0)
#
#     print(f'#{t} {result}')


# ---------------------------------------
# 접근 방법2
# 3월 기준으로 생각 : 2월까지의 최소 금액 + 본인의 금액 중 최소 금액
# 이전의 최소 금액들을 활용해서 내 최소 금액을 구할 수 있음
# DP 활용
# => 왜 DP로?
# DP 조건
# 1. 작은 문제로 분할 가능해야함
#    - 전체 문제의 합 = 각 달까지의 최소 금액이 쌓여서 완성
#    - 각 달까지 최소 금액 문제로 생각
# 2. 뒤에 결과를 구할 때, 앞에서 구했던 결과가 변하면 안됨

T = int(input())

for t in range(1, T + 1):
    cost = list(map(int, input().split()))
    # 인덱스 1 ~ 12까지 보려고 + [0] 해줌
    days = [0] + list(map(int, input().split()))
    dp = [0] * 13       # 1 ~ 12월 최소 금액들을 저장

    # dp[1] = min(days[1] * cost[0], cost[1])
    # dp[2] = min(days[2] * cost)

    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        # 1 ~ 2월까지는 이전 달 + 1일권 구입 / 이번 달 + 1달 권
        # 3월 ㅇㅣ후 : 이전 달 + 1일권 구입 / 이전 달 + 1달 권 / 3달 전에 3달 권 구입 중 최소
        dp[i] = min(dp[i - 1] + (days[i] * cost[0]), dp[i - 1] + cost[1])

        # 인덱스 오류를 피하기 위해, 3월 이후 계산을 따로 작성
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + cost[2])

    result = min(dp[12], cost[3])
    print(f'#{t} {result}')