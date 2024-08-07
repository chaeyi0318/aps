# def push(item, size):
#     global top
#     top += 1
#
#     if top == size:
#         print('overflow')
#     else:
#         stack[top] = item
#
#
# def stc_pop():
#     global top
#
#     if top == -1:
#         print('underflow')
#         return 0
#     elif len(stack) == 0:
#         # underflow
#         return
#     else:
#         top -= -1
#         return stack[top + 1]
#
#
# size = 10
# stack = [0] * size
# top = -1
#
# push(10, size)
# top += 1
# stack[top] = 20
#
# print(stc_pop())
#
# if top > -1:    # pop()
#     top -= 1
#     print(stack[top + 1])

# 쉬운 버전
# stack = []
# stack.append(1)  # push(1)
# stack.append(2)
# stack.append(3)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
