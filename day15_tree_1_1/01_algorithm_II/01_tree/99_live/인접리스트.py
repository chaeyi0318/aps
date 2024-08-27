'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
# 1부터 탐색 시작
def dfs(node):
    # 노드가 -1인 경우 없는 거니까 탐색 안함
    if node == -1:
        return

    preorder.append(node)
    dfs(graph[node][0])
    inorder.append(node)
    dfs(graph[node][1])
    postorder.append(node)



N = int(input())
E = N - 1
arr = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]      # 1부터 시작이라 N + 1만큼 만들기
# append 를 통해 갈 수 있는 경로를 추가하기
for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]       # p 부모, c 자식
    graph[p].append(c)

# 없는 경우 -1로 데이터를 저장하기 위한 코드("좌우 경로가 있는가 ?")
# 탐색 시 index 오류를 방지하기 위해 없는 경로를 -1로 저장하였습니다.
# 값이 하나만 있거나 없는 경우 -1 처리
for i in range(N + 1):
    while len(graph[i]) < 2:
        graph[i].append(-1)

print(graph)


preorder = []   # 전위
inorder = []    # 중위
postorder = []  # 후위

dfs(1)

print(*preorder)
print(*inorder)
print(*postorder)