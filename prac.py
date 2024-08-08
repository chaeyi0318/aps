T = 10

def remove_txt(N, txt):
    stack = []

    for i in range(N):
        if stack[-1] == txt[i]:
            stack.pop()
        else:
            stack.append(txt[i])
    return stack

for t in range(1, T + 1):
    N = int(input().split())
    txt = map(int, input().split())
    print(remove_txt(N, txt))