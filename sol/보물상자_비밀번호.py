T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(input())  # 16진수 문자열을 리스트로 입력 받음
    num_set = set()

    # N자리를 4등분하는 step 계산
    step = N // 4

    # 4회 회전하면서 모든 숫자 조합을 set에 넣음
    for _ in range(step):  # 총 4번의 회전
        for i in range(0, N, step):
            # 각 조각을 16진수로 만들어 set에 추가
            tmp = ''.join(arr[i:i + step])
            num_set.add(tmp)
        arr.append(arr.pop(0))  # 배열을 한 칸 회전

    # set에 있는 값을 10진수로 변환하고 내림차순 정렬
    result = sorted([int(item, 16) for item in num_set], reverse=True)

    # K번째로 큰 값 출력
    print(f"#{t} {result[K - 1]}")