import sys
sys.stdin = open('input.txt')

def f(level):
    global result       # 결과 result global로 만들기

    # level이 cnt 횟수만큼 교환되었을 때 종료
    if level == cnt:
        tmp = int(''.join(arr))     # result랑 비교할 값으로 arr를 사용

        if result < tmp:
            result = tmp

        return

    # i번째랑 i + 1번째 값 교환하는 반복문
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]

            # visited에 넣을 값
            # level 같이 저장한 이유 : 교환 1번 했을 때 123이랑 3번 했을 때 123은 다른 상태임
            # 지금 생각해보니까 어차피 중복체크 하는 거니까 set으로 안했어도 될 듯...? => 그래도 속도는 set이 빠름...
            # 아님. 중복 저장 안하니까 중복 저장 안하려고 하는 조건 없어도 됨 set 사용 맞움
            check_value = (level, ''.join(arr[:]))

            # 방문 체크
            if check_value not in visited:
                visited.add(check_value)
                # level + 1 해서 다음 탐색 ㄱㄱ
                f(level + 1)
            # 배열 다시 원상복구
            # 예를 들어, 배열 [1, 2, 3]에서 첫 번째 자리와 두 번째 자리를 교환하여 [2, 1, 3]이 되었다고 가정해봅시다.
            # 이 상태에서 재귀적으로 탐색한 후에는 원래 상태인 [1, 2, 3]으로 되돌려야 합니다.
            # 그래야 다음으로 첫 번째 자리와 세 번째 자리를 교환하여 [3, 2, 1]과 같은 새로운 상태를 탐색할 수 있습니다.
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for t in range(1, T + 1):
    num, cnt = map(int, input().split())        # num : 숫자 ex) 123 / cnt : 교환횟수 ex) 1
    arr = list(str(num))        # 입력 받은 num을 배열 형태로 바꿈 (인덱스를 교환하기 위해서)
    visited = set()         # 중복 체크
    result = 0      # 결과값

    f(0)
    print(f'#{t}', result)