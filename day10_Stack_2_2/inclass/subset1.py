# 부분집합
# # def dfs(arr, 값의 위치를 결정할 값(인덱스) ,arr의 길이(원소의 개수)):
# #     pass
#
# # 후보 추천을 하면 백트래킹 하기 쉬움?
#
# # maxcandidate = 후보를 저장할 곳의 크기
# # nmax = 부분집합크기 == 사실상 받은 배열의 length
#
#
# def backtracking(a, k, n):
#     c = [0] * MAXCANDIDATES
#
#     if k == n:
#         process_solution(a, k)
#     else:
#         ncandidates
#
#
# def construct_candidates(a, k, n, c):
#     c[0] = True
#
#
# def process_solution(a, k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end=' ')
#         print()
#
#
# MAXCANDIDATES = 2
# NMAX = 4

# 집합 [1,2,3]에서 모든 순열을 생성하는 함수
# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)


# 위 코드 바꿔보기

def backtrack(a, k, n):
    c = [0] * MAXCANDIDATES  # 후보를 저장할 배열

    if k == n:
        for i in range(0, k):
            print(a[i], end=' ')
        print()
    else:
        ncandidates = construct_candidates(a, k, n, c)

        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)


def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)  # used, 사용된적 있는지 T/F

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0

    for i in range(1, NMAX + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


MAXCANDIDATES = 3
NMAX = 3
a = [0] * NMAX
backtrack(a, 0, 3)
