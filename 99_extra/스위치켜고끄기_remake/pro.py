import sys

sys.stdin = open('input.txt')

'''
3   T
12  스위치 개수
1 0 0 1 1 1 0 1 0 0 1 1     스위치 상태
3   학생수
1 3     성별 & 번호
2 8
2 6
'''

T = int(input())

for t in range(1, T + 1):
    s = int(input())
    s_state = list(map(int, input().split()))
    st = int(input())
    st_arr = [list(map(int, input().split())) for _ in range(st)]

    for gender, num in st_arr:
        print(gender, num)

        if gender == 1:  # 남학생
            # prime_num
            pass
        else:           # 여학생
            divisor = []        # 약수 list

            for n in range(1, num + 1):
                if num % n == 0:
                    divisor.append(n)

    print(divisor)
