import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    data = [(list(map(int, input().split()))) for _ in range(100)]

    # for i in range(len(data)):
