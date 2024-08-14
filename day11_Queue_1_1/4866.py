import sys

sys.stdin = open('4866_input.txt')

check_dict = {
    '}': '{',
    ')': '('
}

def check_txt(txt):
    stack = []

    for ch in txt:
        if ch in check_dict.values():
            stack.append(ch)
        elif ch in check_dict.keys():
            if len(stack) == 0 or stack[-1] != check_dict[ch]:
                return 0
            stack.pop()
    if len(stack) == 0:
        return 1
    return 0

T = int(input())

for t in range(1, T + 1):
    txt = input()

    print(f'#{t} {check_txt(txt)}')