import sys
sys.stdin = open('1234_input.txt')


def pw_remove(N, txt):
    stack = []

    for char in txt:
        if len(stack) != 0 and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)
    return result


T = 10

for t in range(1, T + 1):
    N, txt = input().split()

    password = pw_remove(N, txt)
    print(f'#{t}', password)