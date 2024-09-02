# 재귀
path = []
N = 4

def run(lev):
    if lev == N:
        print(*path)
        return

    for i in range(1, 4):
        path.append(i)
        run(lev + 1)
        path.pop()

run(0)


# x는 서로 다른 메모리를 가지는 다른 객체
def func(x):
    x += 1

x = 10
func(x)
print(x)


# 리스트는 x 값이 변함
def func(x):
    x[0] += 1

x = [10]
func(x)
print(x)


# 재귀
def KFC(x):
    if x == 2:
        return
    print(x)
    KFC(x + 1)
    print(x)


KFC(0)
print('끝')


# 도전과제
def func(x):
    if x == 6:
        return
    # 재귀 전
    print(x, end=' ')
    func(x + 1)
    # 재귀 후
    print(x, end=' ')

func(0)

def KFC(x):
    # 기저조건
    if x == 3:      # depth / level
        return

    # KFC(x + 1)
    # KFC(x + 1)
    # KFC(x + 1)
    # KFC(x + 1)
    # => for문으로 변경

    # 후보군
    for i in range(4):
        KFC(x + 1) # 인자 전달

KFC(0)