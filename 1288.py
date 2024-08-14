T = int(input())

for t in range(1, T + 1):
    N = int(input())
    num_set = set()

    i = 1

    while len(num_set) != 10:
        num = (N * i)