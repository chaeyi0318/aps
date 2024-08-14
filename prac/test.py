import sys

sys.stdin = open('input.txt')

switch_cnt = int(input())  # 스위치 개수
switch_list = list(map(int, input().split()))  # 스위치 상태 / 켜져 잇으면 1 꺼져있으면 0
student = int(input())  # 학생 수
# 남학생 1, 여학생 2

for s in range(student):
    gender, num = map(int, input().split())

    # 남학생
    if gender == 1:
        # i는 0부터 시작인데 스위치 번호는 1부터 시작
        for i in range(len(switch_list)):
            if (i + 1) % num == 0:
                switch_list[i] = 1 if switch_list[i] == 0 else 0
    elif gender == 2:
        # 본인 변경
        switch_list[num - 1] = 1 if switch_list[num - 1] == 0 else 0

        # i는 1부터 해서 하나씩 증가
        i = 1
        # 범위 내에 있을 경우 while문
        while (num - 1 - i) >= 0 and (num - 1 + i) < len(switch_list):
            # num -1을 기준으로 앞뒤가 같은 경우에 값 변경
            if switch_list[num - 1 - i] == switch_list[num - 1 + i]:
                switch_list[num - 1 - i] = 1 if switch_list[num - 1 - i] == 0 else 0
                switch_list[num - 1 + i] = 1 if switch_list[num - 1 + i] == 0 else 0
            else:
                break
            # 다음 인덱스 탐색을 위해 i 증가
            i += 1
    # elif gender == 2:
    #     switch_list[num - 1] = 1 if switch_list[i] == 0 else 0
    #     for i in range((switch_cnt // 2) - 1):
    #
    #         back_idx = num - 1 + i
    #         front_idx = num - 1 - i
    #
    #         if back_idx < len(switch_list) and front_idx >= 0 and switch_list[back_idx] == switch_list[front_idx] and front_idx != back_idx:
    #             switch_list[back_idx] = 1 if switch_list[i] == 0 else 0
    #             switch_list[front_idx] = 1 if switch_list[i] == 0 else 0
        # for i in range(num - 1):
        #     if switch_list[num + i] == switch_list[num - i]:
        #         switch_list[i] = 1 if switch_list[i] == 0 else 0
        # 3번 받음 근데 인덱스는 2임
        # for i in range((switch_cnt // 2), 0, -1):
        #     # back_idx = num 기준 뒤에 있는 인덱스
        #     back_idx = num - 1 + i
        #     # front_idx = num 기준 앞에 있는 인덱스
        #     front_idx = num - 1 - i
        #
        #     # 범위 벗어나지 않게 조건문 그리고 서로 같은 경우에만
        #     if back_idx < len(switch_list) and front_idx >= 0 and switch_list[back_idx] == switch_list[front_idx]:
        #         # front부터 back까지 값 변경
        #         for j in range(front_idx, back_idx + 1):
        #             switch_list[j] = 1 if switch_list[j] == 0 else 0
        #         break
# # 출력 1 0 0 0 1 1 0 1
# print(*switch_list)

for i in range(0, len(switch_list), 20):
    print(*switch_list[i:i + 20])
