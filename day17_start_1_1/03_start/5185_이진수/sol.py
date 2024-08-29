import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, hex_num = input().split()

    hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}

    result = []

    for i in range(len(hex_num)):
        result.append(hex_to_bin[hex_num[i]])

    print(f'#{t}', ''.join(result))