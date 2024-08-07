# # 피보나치 수
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# # 팩토리얼
# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n - 1)
#
#
# print(f(3))


# 모든 배열 원소에 접근하기
def arr_data(i, N):  # i : 현재 인덱스 , N : 접근할 인덱스
    if i == N:
        return
    else:
        print(data[i])
        arr_data(i + 1, N)
        return


data = [1, 2, 3]        # 배열은 global 안해도 접근 가능
N = len(data)
arr_data(0, N)     # (현재 idx, 목표 idx)