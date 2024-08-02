# arr = list('algorithm')
#
# print(arr)
#
# for i in range(len(arr) // 2):
#     arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
#
# print(arr)

s1 = 'abc'
s2 = 'abc'
print(s1 == s2)  # True

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)  # True

s3 = s1[:2] + 'c'
print(s2 == s3)     # True
print(s2 is s3)     # False
print(s1 is s2)     # True
