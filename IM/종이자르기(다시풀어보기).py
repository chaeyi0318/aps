# 10 8      # 종이 행열
# 3     자를 점선 개수
# 가로로 자르는 점선은 0, 숫자
# 세로로 자르는 점선은 1, 숫자
# 0 3   가로
# 1 4   세로
# 0 2   가로

row, col = map(int, input().split())    # 행 열
print(row, col)

cut = int(input())      # 자를 횟수

for i in range(cut):
    d, num = map(int, input().split())  # d = 방향 / num = 점선 idx?
    