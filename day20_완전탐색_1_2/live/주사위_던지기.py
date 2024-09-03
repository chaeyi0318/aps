path = []
n = 3

def run(level, start):
    if level == n:
        print(*path)
        return

    for i in range(start, 7):
        path.append(i)
        run(level + 1, i)
        path.pop()

run(0, 1)

