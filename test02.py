import sys
sys.stdin = open('test02_input.txt')

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp_list = [arr[0]]
    result_list = []

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            result_list.append(tmp_list)
            tmp_list = []
        tmp_list.append(arr[i])
    result_list.append(tmp_list)

    # min_value = result_list[0][0]
    # max_value = result_list[0][0]
    # answer = None
    #
    # for i in range(len(result_list)):
    #     min_value = None
    #     max_value = None
    #     for j in range(len(result_list[i])):
    #         if result_list[i][j] > max_value:
    #             max_value = result_list[i][j]
    #         if result_list[i][j] < min_value:
    #             min_value = result_list[i][j]
    #
    #     answer = (max_value - min_value) // len(result_list[i])
    #     # answer = (max_value + min_value) / len(arr[i][j])
    # print(answer)
    # print(max_value, min_value)