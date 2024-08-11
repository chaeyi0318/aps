import sys

sys.stdin = open('21619_input.txt')

def match(arr) :
    stack = []

    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            if not stack:
                return -1
            stack.pop()

    result = 1 if len(stack) == 0 else -1

    return result

T = int(input())

for t in range(1, T + 1):
    arr = input()

    print(f'#{t} {match(arr)}')