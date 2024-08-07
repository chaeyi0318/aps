import sys
sys.stdin = open('21618_input.txt')

T = int(input())


def remove_char(txt):
    stack = []

    for x in txt:
        if len(stack) == 0 or stack[-1] != x:
            stack.append(x)
        elif stack[-1] == x:
            stack.pop()
    return len(stack)


for t in range(1, T + 1):
    txt = input()
    print(f'#{t}', remove_char(txt))