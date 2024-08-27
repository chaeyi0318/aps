import sys

sys.stdin = open('input.txt')


def inorder(node):  # 중위순회
    if node == 0:  # node가 0인 경우는 return
        return

    # 중위순회는 왼쪽 - 본인 - 오른쪽
    inorder(tree[node][0])
    result.append(char[node])
    inorder(tree[node][1])


# 코드 개복잡한듯; 수정 필요
for t in range(1, 11):
    N = int(input())  # 정점 수

    tree = [[0, 0] for _ in range(N + 1)]  # 부모 - 자식 저장
    char = [0] * (N + 1)  # 단어 저장

    for _ in range(N):  # 입력 받은 N만큼 반복
        tmp = list(input().split())  # 입력 받은 값을 tmp에 리스트 형태로 저장
        idx = int(tmp[0])  # tmp[0] == 노드 번호
        char[idx] = tmp[1]  # char 배열에 노드 번호 순으로 문자 저장해줌

        for x in range(1, len(tmp)):  # 자식노드 찾는 반복문
            if tmp[x].isdecimal():  # tmp[x]가 숫자인 경우에만
                if tree[idx][0] == 0:  # tree[idx]에 0번째 값이 0인 경우
                    tree[idx][0] = int(tmp[x])  # tmp[x]값을 형변환 후 넣어줌
                else:
                    tree[idx][1] = int(tmp[x])

    result = []  # 결과 담을 리스트
    inorder(1)  # 1부터 중위순회

    print(f'#{t}', ''.join(result))  # 출력
