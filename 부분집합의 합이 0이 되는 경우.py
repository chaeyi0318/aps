def find_subsets(arr, index=0, current_subset=None, subsets=None):
    if current_subset is None:
        current_subset = []
    if subsets is None:
        subsets = set()  # 중복 제거를 위한 set 사용

    # 현재 부분집합의 합이 0이면 결과에 추가
    if sum(current_subset) == 0 and current_subset:
        subsets.add(tuple(sorted(current_subset)))  # set에 추가하기 위해 tuple로 변환

    # 배열의 끝에 도달하면 종료
    if index == len(arr):
        return

    # 현재 원소를 포함하지 않는 경우
    find_subsets(arr, index + 1, current_subset, subsets)

    # 현재 원소를 포함하는 경우
    current_subset.append(arr[index])
    find_subsets(arr, index + 1, current_subset, subsets)

    # 백트래킹을 위해 마지막 원소 제거
    current_subset.pop()

    return subsets

arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9]
result = find_subsets(arr)

# 중복 없이 결과를 한 번만 출력
if result:
    print("합이 0이 되는 부분집합들:")
    for subset in result:
        print(list(subset))  # tuple을 다시 list로 변환하여 출력
else:
    print("합이 0이 되는 부분집합이 없습니다.")
