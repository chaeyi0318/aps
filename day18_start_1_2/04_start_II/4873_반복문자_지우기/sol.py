import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    arr = list(input())
    stack = []

    for i in range(len(arr)):
        if len(stack) == 0 or stack[-1] != arr[i]:
            stack.append(arr[i])
        elif arr[i] == stack[-1]:
            stack.pop()
    print(f'#{t}', len(stack))