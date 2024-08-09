def f(i, N):  # bit[i]를 결정하는 함수
    if i == N:  # 모든 원소에 대해 결정하면
        result = 0  # 부분집합의 합을 저장할 변수
        for j in range(N):
            if bit[j]:  # bit[j]가 0이 아니면
                result += a[j]
                print(a[j], end=' ')
        print(f' : ', result)
    elif i:
        return
        # print()  # 부분집합을 한 행에 표시하는 print
    else:
        # bit[i] = 1
        # f(i + 1, N)
        # bit[i] = 0
        # f(i + 1, N)
        for j in [1, 0]:
            bit[i] = j
            f(i + 1, N)


a = [1, 2, 3]  # 주어진 원소의 집합
N = len(a)
bit = [0] * N  # 원소의 포함 여부를 표시하는 배열

f(0, N)  # N개의 원소에 대해 부분집합을 만드는 함수
