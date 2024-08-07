import sys

sys.stdin = open('5432_input.txt')


def cut_stick(stick):
    result = 0
    stack = []
    cnt = 0

    for i in range(1, len(stick)):
        if stick[i] == '(':
            cnt += 1
        else:
            cnt -= 1

        stack.append(stick[i])

        if len(stack) >= 0:
            if stack[i - 1] == '(':
                result += cnt
            else:
                result += 1

    return result


T = int(input())

for tc in range(1, T + 1):
    stick = list(input())

    print(cut_stick(stick))

    # print(stick)
