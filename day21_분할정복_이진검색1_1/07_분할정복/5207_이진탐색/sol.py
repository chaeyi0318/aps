import sys

# 입력 파일을 표준 입력으로 열어서 읽어옴
sys.stdin = open('input.txt')


def binary_search(left, right, target, dir):
    # 이진 탐색을 수행하는 함수
    # left: 탐색 구간의 왼쪽 끝 인덱스
    # right: 탐색 구간의 오른쪽 끝 인덱스
    # target: 찾고자 하는 값
    # dir: 이전 탐색 방향 ('L' 또는 'R')

    # 탐색 범위를 벗어나면 False 반환
    if left > right:
        return False

    # 중간값 계산
    mid = (left + right) // 2

    # target 값을 찾으면 True 반환
    if target == A[mid]:
        return True

    # 중간값이 target보다 크면 왼쪽 부분을 탐색
    if A[mid] > target:
        # 이전에 이미 왼쪽을 탐색했다면 False 반환
        if dir == 'L':
            return False
        else:
            # 왼쪽으로 계속 탐색, 방향을 'L'로 설정
            return binary_search(left, mid - 1, target, 'L')
    else:
        # 중간값이 target보다 작으면 오른쪽 부분을 탐색
        # 이전에 이미 오른쪽을 탐색했다면 False 반환
        if dir == 'R':
            return False
        else:
            # 오른쪽으로 계속 탐색, 방향을 'R'로 설정
            return binary_search(mid + 1, right, target, 'R')


# 테스트 케이스의 수를 입력 받음
T = int(input())

# 각 테스트 케이스마다 수행
for t in range(1, T + 1):
    # N: 리스트 A의 원소 개수, M: 리스트 B의 원소 개수
    N, M = map(int, input().split())  # A랑 B에 속한 원소 개수

    # 리스트 A의 원소들을 입력받아 정렬
    A = sorted(list(map(int, input().split())))  # N개의 리스트

    # 리스트 B의 원소들을 입력받음
    B = list(map(int, input().split()))  # M개의 리스트

    '''
    리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인
    B가 A에 들어있는지 확인하는 과정
    '''

    # A에 존재하는 B의 원소 개수를 세기 위한 변수
    cnt = 0

    # B의 각 원소에 대해 A에 존재하는지 확인
    for i in range(len(B)):
        # 이진 탐색 수행, 존재하면 cnt 증가
        if binary_search(0, len(A) - 1, B[i], ''):
            cnt += 1

    # 각 테스트 케이스의 결과 출력
    print(f'#{t}', cnt)
