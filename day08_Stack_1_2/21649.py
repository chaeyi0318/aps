def DFS(s, V):
    visited = [0] * (V + 1)
    result = [s]
    stack = []
    result = [s]
    visited[s] = 1
    v = s

    while True:
        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                result.append(v)
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
    return result


V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(V + 1)]

for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)

print('#1',end=' ')
print('-'.join(map(str, DFS(1, V))))