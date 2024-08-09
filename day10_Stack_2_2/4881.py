import sys

sys.stdin = open('4881_input.txt')


# 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
def find_min_value(depth, current_list, current_sum):

    num = arr[depth]

    print(num)

    # 현재 행을 선택한 경우
    # find_min_value(depth + 1, current_list + [num], current_sum + [num])

    # # 현재 행을 선택하지 않은 경우..?
    # find_min_value(depth + 1, current_list, current_sum)

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []


    find_min_value(depth=0, current_list=[], current_sum=0)

    # print(result)
