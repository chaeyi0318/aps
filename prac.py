# T = 10
#
# def remove_txt(N, txt):
#     stack = []
#
#     for i in range(N):
#         if stack[-1] == txt[i]:
#             stack.pop()
#         else:
#             stack.append(txt[i])
#     return stack
#
# for t in range(1, T + 1):
#     N = int(input().split())
#     txt = map(int, input().split())
#     print(remove_txt(N, txt))

arr = [[1, 3, 6], [2, 5, 7], [5, 3, 9]]
N = 3
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         print(arr[i + j][j] ,end=' ')
#         # for k in range(1, N - 1):
#         #     print(arr[i + k][j])

# for i in range(len(arr)):
#     for j in range(N - 1):
#         print(arr[i + j][i], end=' ')

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[j][i], end=' ')
    print()
