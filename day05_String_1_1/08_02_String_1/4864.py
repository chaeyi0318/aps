import sys
sys.stdin = open('4864_input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    print(f'#{tc}', 1 if str1 in str2 else 0)