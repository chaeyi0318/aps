import sys
sys.stdin = open('1225_input.txt')

for t in range(10):
    t = int(input())
    pw = list(map(int, input().split()))
    cnt = 1

    while pw[-1] != 0:
        data = pw.pop(0)
        data -= cnt

        if data < 0:
            data = 0

        pw.append(data)
        cnt += 1

        if cnt > 5:
            cnt = 1

    print(pw)