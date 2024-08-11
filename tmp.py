def solution(arr):
    answer = []

    for i in range(len(arr)):
        if len(answer) == 0 or answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer

print(solution([1,1,3,3,0,1,1]))