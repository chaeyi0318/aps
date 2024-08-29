import sys

sys.stdin = open('input.txt')


def cal(left, right, oper):
    if oper == '+':
        return left + right
    elif oper == '-':
        return left - right
    elif oper == '*':
        return left * right
    elif oper == '/':
        return left // right

    # return eval(f'{left} {oper} {right}')


# 후위순회 만들기
def postorder(node):
    # 이번에는 트리 구성할 때 없는 자식 번호 기록 안했음
    # 왼쪽, 오른쪽 자식이 반드시 있는 경우가 있음
    # 언제? 연산자인 경우에
    # in - 시퀀스 연산자

    # if arr[node][1] in ['+', '-', '*', '/']: 이 조건문도 가능
    if type(arr[node][1]) == type(''):  # 얘가 연산자임을 알 수 잇는 방법
        left = postorder(arr[node][2])  # 왼쪽 자식
        right = postorder(arr[node][3])  # 오른쪽 자식
        return cal(left, right, arr[node][1])

    else:  # 피연산자
        return arr[node][1]


for t in range(1, 11):
    N = int(input())
    # node 번호 인덱스로 사용할 값만 int로 형변환 해서 tree 정보 기록
    arr = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]
    arr.insert(0, 0)  # 0번 노드는 사용하지 않을 것이므로, 0번째에 사용 안하는 값 삽입
    # print(arr)
    result = postorder(1)
    print(f'#{t}', int(result))
