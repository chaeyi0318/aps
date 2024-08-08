arr = [1, 2, 3, 5, 3, 4, 7, 7, 9, 2, 5, 7, 5, 5, 5]

result = []
tmp = [arr[0]]

for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
        result.append(tmp)
        tmp = []
    tmp.append(arr[i])

result.append(tmp)

print(result)