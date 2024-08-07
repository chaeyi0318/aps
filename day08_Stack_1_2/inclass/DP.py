# 동적 계획(Dynamic Programming) 알고리즘
# 피보나치 수 DP
def fibo(n):
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
