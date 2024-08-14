import sys
from collections import deque

sys.stdin = open('5099_input.txt')

T = int(input())
# '''
# 1. 피자의 번호를 출력해야 하기 때문에 피자의 번호와 함께 치즈를 같이 저장한다.
#
# 2. 화덕보다 피자의 양이 더 많기 때문에 처음에 화덕에 들어갈 수 있는 피자와 남는 피자로 나눈다.
#
# 3. 화덕의 피자를 앞에서 하나씩 보며 치즈의 반이 0이 아니면 리스트의 뒤로 추가한다.
#
# 4. 만약 치즈의 반이 0이라면 그 피자를 pop하고 남은 피자중 가장 앞에 있는 피자를 화덕에 추가해준다.
#
# 5. 그렇게 돌리다가 화덕에 피자가 1개만 남게되면 while문을 종료한다.
#
# 6. 화덕에 있는 단 하나의 피자가 결국 마지막까지 남게 된 피자이므로 피자의 인덱스를 출력한다.
# '''
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     cheese = list(map(int, input().split()))
#
#     for i in range(len(cheese)):
#         cheese.append([i + 1, cheese[i]])
#     print(cheese)


# T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    cheese_idx = deque()
    oven = deque()

    for i in range(M):
        cheese_idx.append([i + 1, cheese[i]])
    print(cheese_idx)

    # i = 0

    # while True:
    #     if i >= N:
    #         i = 0
    #     cheese_idx[0]
#
#     # print(cheese.index(7)) index(7)의 제일 처음 나오는 인덱스 값
#     # 오븐에 피자 넣을 때 인덱스 값 구해서 idx 배열에 저장함
#     # 치즈가 0이 되면 oven에서 pop하고 idx에서도 pop함
#     # len(oven)이 1이 되면 종료?
#
#     for i in range(N):
#         oven.append(cheese[i])
#         idx.append(i)
#
#     print(oven)
#     print(idx)
#
#     i = 0

    # while len(cheese) > 1:
    #     if i >= N:
    #         i = 0
    #     cheese[i] //= 2
    #
    #     if cheese[i] == 0:
    #         cheese.pop(i)
    #     i += 1
    #
    # print(oven)
    #
    # oven = deque(cheese)
    # print(oven)

