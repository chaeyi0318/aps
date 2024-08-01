# while 사용할 때 i < n and a[i] < key : 순서 지키기


#
def selection_sort(arr, N):  # arr 정렬대상, N len
    # 주어진 구간에 대해 기준위치 i 지정
    for i in range(N - 1):
        min_idx = i     # 최솟값 위치를 기준 위치로 가정

        for j in range(i + 1, N):   # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]     # 구간의 최솟값을 교환

    print(arr)


A = [2, 7, 5, 3, 4]
B = [4, 3, 2, 1]
selection_sort(A, len(A))
selection_sort(B, len(B))


# 연습문제3 델타 활용하기