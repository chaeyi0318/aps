import sys
sys.stdin = open('Flatten_input.txt')

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
