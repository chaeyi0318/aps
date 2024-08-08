import sys

sys.stdin = open('4874_input.txt')

operator = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

T = int(input())


def calculate(txt):
    stack = []
    answer = 0

    for data in txt:
        if data == '.':
            if len(stack) != 1:
                return 'error'
            else:
                answer = stack.pop()
        elif data in operator:
            if len(stack) < 2:
                return 'error'
            else:
                if len(stack) >= 2:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())

                    if data == '+':
                        result = num2 + num1
                    elif data == '-':
                        result = num2 - num1
                    elif data == '*':
                        result = num2 * num1
                    elif data == '/':
                        if num1 == 0 or num2 == 0:
                            return 'error'
                        result = num2 // num1
                    stack.append(result)
                else:
                    return 'error'
        elif data.isdigit():
            stack.append(data)
        else:
            return 'error'

    return answer

for t in range(1, T + 1):
    txt = list(input().split(' '))
    print(f'#{t}', calculate(txt))

# operator = {
#     '+': 1,
#     '-': 1,
#     '*': 2,
#     '/': 2
# }
#
# T = int(input())
#
# def calculate(txt):
#     stack = []
#
#     for data in txt:
#         if data == '.':
#             if len(stack) != 1:
#                 return ['error']
#             else:
#                 return stack
#         elif data in operator:
#             if len(stack) < 2:
#                 return ['error']
#             else:
#                 num1 = int(stack.pop())
#                 num2 = int(stack.pop())
#
#                 if data == '+':
#                     result = num2 + num1
#                 elif data == '-':
#                     result = num2 - num1
#                 elif data == '*':
#                     result = num2 * num1
#                 elif data == '/':
#                     if num1 == 0 or num2 == 0:
#                         return ['error']
#                     result = num2 / num1
#                 stack.append(result)
#         elif data.isdigit():
#             stack.append(data)
#
#
# for t in range(1, T + 1):
#     txt = list(input().split(' '))
#     print(f'#{t}', *calculate(txt))
