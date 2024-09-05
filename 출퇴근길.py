from sys import stdin

T = int(stdin.readline())
bus = list(map(int, stdin.readline().split()))
cnt = 0

for i in range(T):
    tmp = 0
    for j in range(i + 1, T):
        if bus[i] < bus[j]:
            tmp += 1
        elif bus[i] > bus[j]:
            cnt += tmp

print(cnt)