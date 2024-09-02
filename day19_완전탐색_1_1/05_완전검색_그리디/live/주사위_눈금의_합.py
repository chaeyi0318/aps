'''
3개의 주사위를 던져서 나올 수 있는 중복 순열에 대해, 합이 10 이하가 나오는 경우는 몇가지?
기저조건 : 주사위 3개를 던졌을 때
후보군 : 1 ~ 6
=> 주사위 3개가 서로 영향이 없는 독립적인 것이라 완전탐색ㄱㄱ
'''

path = []

# 주사위 몇 개 던졌는지, 주사위 합이 몇인지?
def recur(level, total):
    # 백트래킹 : 이미 10을 넘은 경우의 수는 계산할 필요가 없음
    if total > 10:
        return
    
    # 기저조건 : 주사위 3개 던졌을 때
    if level == 3:
        # 합이 10 이하
        if total <= 10:     # 여기 빼도 됨 (가지치기 있을 때는)
            print(path)

        return

    # 후보군 탐색
    for i in range(1, 7):
        # i의 의미 : 주사위 숫자
        path.append(i)
        recur(level + 1, total + i)     # 주사위 결과를 더하여 전달
        path.pop()

# 0개 던졌고 total은 0
recur(0, 0)