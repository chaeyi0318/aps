N = int(input())
card = list(map(int, input().split()))
M = int(input())
number = list(map(int, input().split()))

card.sort()

start = len(card) // 2



# for i in range(M):
#     cnt = 0
#
#     for j in range(N):
#         if m_arr[i] == n_arr[j]:
#             cnt += 1
#
#     print(cnt, end=' ')