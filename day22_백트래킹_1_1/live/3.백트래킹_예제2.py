# 1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력하시오.
# 단, 순서에 따른 중복을 제거하세요
arr = [i for i in range(1, 11)]
visited = []
path = []

# 버전1
def dfs(level, sum, idx):
    # 가지치기 : 합이 10이면 종료
    if sum == 10:
        print(*visited)
        return

    # 가지치기 : 10이상의 숫자면 볼 필요 없음
    if sum > 10:
        return

    # idx부터 시작하는 이유 : 현재 수보다 작은 수들은 이미 고려가 되었음.
    for i in range(idx, len(arr)):
        # 가지치기 : 이미 사용한 숫자라면 생략ㅉ
        if arr[i] in visited:
            continue

        visited.append(arr[i])
        dfs(level + 1, sum + arr[i], i)
        visited.pop()


# 버전2
# 이진 트리 구조처럼 사용(후보를 사용하느냐 vs 마느냐) 하면 훨씬 쉽고 빠르다.
# 부분집합 같은 경우 사용 가능(배치 보는 문제는 사용 못함)
def dfs2(level, sum):
    if sum > 10:
        return

    if sum == 10:
        print(*path)
        return

    # 모두 선택하지 않으면 합이 10이 넘지 못하므로
    # 기저조건 추가
    if level == len(arr):
        return

    # 선택하는 경우
    path.append(arr[level])
    dfs2(level + 1, sum + arr[level])
    path.pop()

    # 현재 숫자를 선택하지 않는 경우
    dfs2(level + 1, sum)


# dfs(0, 0, 0)
dfs2(0, 0)