import sys

sys.stdin = open('4866_input.txt')

T = int(input())

search_dict = {
    '}': '{',
    ')': '('
}

def check(txt):
    stack = []

    for char in txt:
        if char in search_dict.values():
            stack.append(char)
        elif char in search_dict.keys():
            if not stack or stack[-1] != search_dict[char]:
                return 0
            stack.pop()

    if len(stack) == 0:
        return 1
    return 0


for t in range(1, T + 1):
    txt = input()
    print(f'#{t}', check(txt))
