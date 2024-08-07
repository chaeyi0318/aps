def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0

    while progresses:
        if progresses[0] + (day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)
    return answer


# time = 0
# count = 0
#

# answer = []
# stack = []
#
# for i in range(len(progresses)):
#     cnt = 0
#     while progresses[i] < 100:
#         progresses[i] += speeds[i]
#         cnt += 1
#
#     stack.append(cnt)
#
# result = 0
# for i in range(len(stack) - 1):
#     if stack[i] < stack[i + 1]:
#         result += 1
#     else:
#         answer.append(result)
#         result = 0
#
# return answer
# return stack

# print(stack)

# result = 0
# result = 0
#
# for i in range(len(stack) - 1):
#     if stack[i] < stack[i + 1]:
#         result += 1

# for i in range(len(stack) - 1, 0, -1):
#     if stack[i] < stack[i - 1]:
#         result += 1
#         # stack.pop()
#     else:
#         answer.append(result)
#         # stack.pop()
#         result = 0

# while stack:
#     top = len(stack) - 1
#     if stack[top] < stack[top - 1]:
#         result += 1
#         stack.pop()
#     else:
#         answer.append(result)
#         stack.pop()
#         result = 1

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
