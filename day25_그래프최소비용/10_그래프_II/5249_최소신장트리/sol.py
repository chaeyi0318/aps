import sys

sys.stdin = open('input.txt')

# 부모 찾기
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())

    edge = [list(map(int, input().split())) for _ in range(E)]

    edge.sort(key=lambda x: x[2])

    # print(edge)
    parents = [i for i in range(V + 1)]

    cnt = 0
    total = 0

    # print(parents)

    for x, y, weight in edge:
        if find_set(x) != find_set(y):
            cnt += 1
            union(x, y)
            total += weight

            if cnt == V:
                break
    print(f'#{t}', total)
