# hoare 방식의 퀵

# left : 왼쪽 시작 지점
# right : 오른쪽 시작 지점

# 호어 방식의 배열 쪼개기
def hoare_partition(left, right):  # 개념적으로 배운 quick sort
    pivot = arr[left]  # 피봇은 왼, 오, 중 어디두든 상관 없음
    left += 1

    # 조사 시작
    while True:
        # left idx가 right idx보다 작고
        while left <= right and arr[left] < pivot:
            # left 번째 값이 pivot 보다 작다면,
            left += 1

        while left <= right and arr[right] > pivot:
            right -= 1

        # 조사 진행 중 left와 right가 엇갈린 상관이 발생한다면 그 두 위치 swap 안함
        if left >= right:
            return right    # pivot_idx

        arr[left], arr[right] = arr[right], arr[left]


def quick_sort(left, right):
    # 조사 대상이 하나 이하가 된다면 더이상 조사할 수 없음
    if left >= right: return

    # 호어 방식의 정렬을 위해서는, 정렬을 위한 배열을
    # 영역별로 구분 지을 수 있어야 하고,
    # 호어 방식의 파티션 구분 결과로 얻은 idx 지점을 pivot으로 보내겠다.
    pivot_idx = hoare_partition(left, right)

    arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]

    print(arr)
    
    quick_sort(left, pivot_idx - 1)
    quick_sort(pivot_idx + 1, right)


arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]

quick_sort(0, len(arr) - 1)
