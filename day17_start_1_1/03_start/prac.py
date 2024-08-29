# 10진수로 형변환
print(int('10'))

# 2진수로 변환
print(bin(10))  # str 타입임
# 0b1010 -> 0b라는 문자열로 2진수를 나타냈음을 표기

# 진수
print(oct(10))

# 16진수
print(hex(10))

# 16진법 -> 10진법
print(int('F', base=16))

# 2진법 -> 10진법
print(int('1010', base=2))

print(bin(8)[2:])  # 4bit로 표기 -> 전처기
print(bin(1)[2:].zfill(4))

for i in range(16):
    print(i, bin(i)[2:].zfill(4))

bin_to_hex = dict()

for i in range(16):
    print(f'16진수 변환 소문자: {i:x}')
    print(f'16진수 변환 대문자: {i:X}')
    print(f'2진수 변환 : {i:04b}')  # 빈 공간 0로 채우기
    bin_to_hex[f'{i:04b}'] = f'{i:X}'
    # bin_to_hex[bin(i)[2:].zfill(4)] = hex(i)[2:]

print(bin_to_hex)

hex_to_bin = {f'{i:X}': f'{i:04b}' for i in range(16)}

print(hex_to_bin)
