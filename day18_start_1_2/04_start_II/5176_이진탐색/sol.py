import sys

sys.stdin = open('input.txt')


def binary_tree(node):
    global num

    if node <= N:
        binary_tree(node * 2)
        tree[node] = num
        print(tree)
        num += 1
        binary_tree(node * 2 + 1)

        print(tree)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)

    num = 1

    binary_tree(1)

    # print(tree)
    print(f'#{t}', tree[1], tree[N // 2])
