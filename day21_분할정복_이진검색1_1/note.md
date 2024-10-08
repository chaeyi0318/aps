## 병합 정렬(Merge Sort)
### 병합 정렬
- **여러 개의 정렬된 자료의 집합을 병합**하여 한 개의 정렬된 집합으로 만드는 방식
- 분할 정복 알고리즘 활용
    - 자료를 최소단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
    - top-down 방식
- 시간 복잡도 : O(nlongn)


### 병합 정렬 과정
[69, 10, 30, 2, 16, 8, 31, 22]
- 분할 단계 : 전체 자료 집합에 대하여, 최소 크기의 부분 집합이 될 때까지 분할 작업을 계속한다.

>[69 , 10 , 30 , 2] / [16, 8, 31, 22]

>[69, 10] / [30, 2] / [16, 8] / [31, 22]

>[69] [10] [30] [2] [16] [8] [31] [32]

- 병합 단계 : 2개의 부분 집합을 정렬하면서 하나의 집합으로 병합
- 8개의 집합이 1개로 병합될 때까지 반복함


## 퀵 정렬
### 퀵 정렬
- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
- 병합 정렬과 다른점
    - 병합 정렬은 그냥 두 부분으로 나누는 반면, 퀵 정렬은 분할할 때, 기준 아이템 중심으로 분할한다.
    - 각 부분 정렬이 끝난 후, 병합정렬은 병합이란 후처리 작업이 필요하나, 퀵 정렬은 필요로 하지 않는다.
- 퀵 정렬은 Partitioning 과정을 반복하면서, 평균 시간복잡도 O(nlogn) 속도라는 빠른 속도로 정렬이 된다.
- 최악의 경우(역순정렬된 데이터) : O(n**2)


### 퀵 정렬 - Partitioning
1. 작업영역을 정한다.
2. 작업영역 중 가장 왼쪽에 있는 수를 Pivot이라고 하자 (Pivot을 기준으로 해석)
3. Pivot을 기준으로 왼쪽에는 Pivot보다 작은 수를 배치한다. 오른쪽에는 Pivot보다 큰 수를 배치 시킨다. (정렬은 안됨)
4. 파티셔닝이 끝나고 Pivot의 위치는 확정됨 즉, 정렬이 다 되었을 때 Pivot의 위치는 지금 그대로 배정
* Hoare partitioning 보기


## 이진 검색(Binary Search)
- 자료의 가운데에 있는 항목의 키 값과 비교히여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수앻함
- **이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.
- **logN**


### 검색 과정
1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 1 ~ 3의 과정 반복
