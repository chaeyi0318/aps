'''
먼저 path라는 전역 리스트 준비
그리고 level 2, Branch 3으로 동작되는 재귀 코드 구현
재귀호출을 하기 직전에 이동할 곳의 위치를 path에 기록(path.append(i))
재귀호출 되면 코드가 진행되어, append 수행
출력하는 코드를 기저조건에서 수행
함수가 리턴되고 즉시 종료
이 후 path에 적은 마지막 기록이 삭제(되돌아 온 후 기록 삭제)
'''
# path = []
#
# def func(x):
#     if x == 2:
#         print(path)
#         return
#
#     for i in range(3):
#         path.append(i)  # 숫자 사용
#         func(x + 1)
#         path.pop()  # 쓰지 않은 시점으로 ㄱㄱ
#
# func(0)

'''
[1 1 1] ~ [6 6 6]
1. 기저조건: 3
2. 후보군 : 1 ~ 6
'''
path = []
visited = [0] * 7 # 1 ~ 7 숫자의 사용 여부를 기록할 리스트


def recur(level):
    # 기저조건
    if level == 3:
        print(*path)
        return
    
    # 후보군
    for i in range(1, 7):
        # 아래 if문을 사용할 때 단점 : "in" = O(len(path)) => 시간 초과 위험도가 높음
        # if i in path:       # 중복 제거
        #     continue

        # if문 변경
        if visited[i]:
            continue
        # 재귀 전 경로 기록 + 사용 기록
        visited[i] = 1
        path.append(i)
        
        # 재귀
        recur(level + 1)
        
        # 돌아오면 경로 삭제 + 사용 여부 초기화
        path.pop()
        visited[i] = 0

recur(0) # 시작점을 전달


'''
[1 1 1 1 1] ~ [4 4 4 4 4]
1. 기저조건 5
2. 후보군 : 1 ~ 4
'''

# path = []
#
# def f(x):
#     if x == 5:
#         print(path)
#         return
#
#     for i in range(1, 5):
#         path.append(i)
#         f(x + 1)
#         path.pop()
#
# f(0)