arr = ['A', 'B', 'C']
n = len(arr)


def get_sub(target):
    for i in range(n):
        if target & 0x1:       # 1을 넣어도 상관 없음
            print(arr[i], end=' ')
        target >>= 1

# target = 0, 1, 2, 3, 4, 5, 6, 7
for target in range(0, 1 << n):  # range(0, 8) : 전체 부분집합을 확인
    print('{', end=' ')
    get_sub(target)
    print('}')
