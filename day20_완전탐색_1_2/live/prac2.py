'''
000 - 공집합
001 - {A}
010 - {B}
011 - {A, B}
100 - {C}
101 - {A, C}
110 - {B, C}
111 - {A, B, C}
만들 수 있는 집합의 총 개수 = pow(2, N)
1 << N 을 활용하여 빠르게 구할 수 있음
'''

# print(bin(1 << 5))
# print(1 << 5)

arr = ['A', 'B', 'C']
N = len(arr)

def get_sub(tar):
    for i in range(N):
        if tar & 0x1:
            print(arr[i], end='')
        tar >>= 1

get_sub(6)
