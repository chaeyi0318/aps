import math

def Forth(li):
    stack = []
    operator = ["+", "-", "*", "/"]

    for i in li:
        if i == ".":
            if len(stack) != 1:
                return ["error"]
            else:
                return stack

        elif i in operator:
            if len(stack) < 2:
                return ["error"]
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+":
                    c = a + b
                elif i == "-":
                    c = a - b
                elif i == "*":
                    c = a * b
                else:
                    c = a // b
                stack.append(c)
        else:
            stack.append(i)


T = int(input())
for _ in range(T):
    li = list(map(str, input().split()))
    print(f"#{_ + 1}", *Forth(li))