STACK_SIZE = 10
stack = [0] * STACK_SIZE
top = -1

top += 1
stack[top] = 1
top += 1
stack[top] = 2
top += 1
stack[top] = 3

top -= 1
print(stack[top + 1])
# print(stack[top])     # 같은 동작
# top -= 1