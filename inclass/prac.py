# 부분집합

# # 3개의 선택된 값을 저장할 리스트 초기화
# selected = [0] * 3
#
# # i, j, m은 각각 첫 번째, 두 번째, 세 번째 선택된 값을 나타냄
# for i in range(2):
#     selected[0] = i
#     for j in range(2):
#         selected[1] = j
#         for m in range(2):
#             selected[2] = m
#             subset = []
#             for n in range(3):
#                 if selected[n] == 1:
#                     subset.append(n + 1)
#             print(subset)

# arr 배열에서 모든 부분 집합을 생성하는 코드
# arr = [1, 2, 3]
# n = len(arr)
# subset_cnt = 2 ** n     # 생성 가능한 부분 집합의 총 개수
#
# subsets = []       # 모든 부분 집합을 저장할 리스트
#
# for i in range(subset_cnt):     # 모든 가능한 부분 집합을 생성하기 위한 반복문
#     subset = []     # 현재 부분 집합을 저장할 리스트
#     for j in range(n):      # 각 요소에 대해 포함 여부를 결정하기 위한 반복문
#         if i & (1 << j):    # i의 j번쩨 비트가 1인지 확인
#             subset.append(arr[j])
#     subsets.append(subset)
#
# print(subsets)

# print(1<<3)


# arr = [i for i in range(1, 10)]
# # print(arr)
#
# n = len(arr)
# subset_cnt = 2 ** n
# subsets = []
#
# for i in range(subset_cnt):
#     subset = []
#
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(arr[j])
#             print(subset)
#             # print(arr[j])
#     subsets.append(subset)
#
# print(subsets)

# arr = [i for i in range(1, 6)]
# n = len(arr)
# subset_cnt = 2 ** n
# subsets = []
#
# for i in range(subset_cnt):
#     subset = []
#
#     for j in range(n):
#         if i & (1 << j):
#             subset.append(arr[j])
#     subsets.append(subset)
# print(subsets)


# binary
def binary_search_recursive(input_list, low, high, key):
    if low > high:
        return False

    mid = (low + high) // 2

    if key == input_list[mid]:
        return input_list[mid]
    elif key < input_list[mid]:
        return binary_search_recursive(input_list, low, mid - 1, key)
    elif key > input_list[mid]:
        return binary_search_recursive(input_list, mid + 1, high, key)


num_list = [i for i in range(11)]

result = binary_search_recursive(num_list, 0, len(num_list) - 1, 2)
print(result)