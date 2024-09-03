arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_sub(target):
    cnt = 0     # 1의 개수
    for i in range(n):
        if target & 1:
            # print(arr[i], end=' ')
            cnt += 1

        target >>= 1

    return cnt

result = 0

for target in range(0, 1 << n):
    if get_sub(target) >= 2:
        result += 1

print(result)