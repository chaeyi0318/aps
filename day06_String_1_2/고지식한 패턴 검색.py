# t = 'TTTTAACCA'
# p = 'TTATTTCTA'
#
# n = len(t)
# m = len(p)
#
# i, j = 0, 0
# while i < n and j < m:
#     # if t[i] != p[j]:
#     #     i = i - j
#     #     j = -1
#     # i += 1
#     # j += 1
#     if t[i] == p[j]:
#         i += 1
#         j += 1
#     else:
#         i = i - j + 1
#         j = 0
t = 'TTTTABC'
p = 'TTA'

N = len(t)
M = len(p)
cnt = 0

for i in range(N - M + 1):  # 비교 시작위치
    for j in range(M):
        if t[i + j] != p[j]:
            break  # for j, 다음 글자부터 비교 시작
    else:  # for j가 중단 없이 반복되면
        cnt += 1
print(cnt)
