N = int(input())
arr = list(map(int, input().split()))


# 연속해서 커지는 수열 찾는 함수
def get_increase_count(arr):
    i_cnt = 1  # 증가 cnt
    tmp = 1

    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            tmp += 1
        else:
            if tmp >= i_cnt:
                i_cnt = tmp
                tmp = 1 # 이거 문제였음
    if tmp >= i_cnt:
        i_cnt = tmp

    return i_cnt


# 연속해서 작아지는 수열 찾는 반복
def get_decrease_count(arr):
    d_cnt = 1  # 감소 cnt
    tmp = 1

    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            tmp += 1
        else:
            if tmp >= d_cnt:
                d_cnt = tmp
                tmp = 1 # 여기 문제

    if tmp >= d_cnt:
        d_cnt = tmp

    return d_cnt

inc_num = get_increase_count(arr)
dec_num = get_decrease_count(arr)

if inc_num > dec_num:
    print(inc_num)
else:
    print(dec_num)

# 두 개 함수 합치기 = 얜 정답 통과
# N = int(input())
# arr = list(map(int, input().split()))
#
# def find_longest_cnt(arr):
#     inc_cnt = 1
#     dec_cnt = 1
#     max_cnt = 1
#
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i - 1]:
#             inc_cnt += 1
#             dec_cnt = 1  # 감소 수열 초기화
#         elif arr[i] < arr[i - 1]:
#             dec_cnt += 1
#             inc_cnt = 1  # 증가 수열 초기화
#         else:
#             inc_cnt += 1
#             dec_cnt += 1
#
#         max_cnt = max(max_cnt, inc_cnt, dec_cnt)
#
#     return max_cnt
#
# print(find_longest_cnt(arr))
