'''
11011110
11011
'''
print(0b11011110 & 0b11011)
print(bin(0b11011110 & 0b11011))

'''
0x4A3 | 25
'''

print(0x4A3 | 25)
print(bin(0x4A3), bin(25))
print(bin(0x4A3 | 25))

print()
print(1)
print(1 << 1, bin(1 << 1))   # 2
print(1 << 2, bin(1 << 2))   # 4
print(1 << 3, bin(1 << 3))   # 8
print(1 << 4, bin(1 << 4))   # 16

print()
print(7 >> 2, bin(7 >> 2))

print()
arr = [1, 2, 3, 4]
# 각 자리를 쓴다 / 안쓴다 -> 나올 수 있는 경우의 수 = 2가지
# 각 자리마다 2가지 경우의 수 -> N 길이라면 -> 2^N만큼의 경우의 수가 나올 수 있다.
print('부분집합의 수', 1 << len(arr))

for i in range(1 << len(arr)):
    print(i, end=' ')
print()

# i & (1 << N): N 번째 비트가 0인지 아닌지 알 수 있다.
# i의 의미 : i번째 부분집합
for i in range(1 << len(arr)):      # range에 2의 len(arr)제곱이 들어가도 노상관
    for idx in range(len(arr)):
        # i & (1 << idx) : i 번째 부분집합에 idx 요소 포함 유무
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()

print()
print(bin(4))
print(bin(~4))
print(~4)   # -5됨 왜?