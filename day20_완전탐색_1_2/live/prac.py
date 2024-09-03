# 재귀
arr = ['O', 'X']        # 역순 출력은 ['X', 'O']
path = []
name = ['MIN', 'CO', 'TIM']

def print_name():
    print('{', end=' ')

    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
    print('}')

def run(lev):       # lev : lev 1,2,3번째 요소
    if lev == 3:        # 원소 3개 모두 고려
        print_name()
        return

    for i in range(2):      # 데려갈지말지
        path.append(arr[i])     # 경로 추가
        run(lev + 1)        # 다음 레벨 고려, 데려갈지말지 저장
        path.pop()

run(0)