def quicksort(A, l, r):
    if l < r:
        # 기준원소의 위치 확정
        p = partition(A, l, r)
        # 왼쪽 부분 정렬
        quicksort(A, l, p - 1)
        # 오른쪽 부분 정렬
        quicksort(A, p + 1, r)

def partition(A, l, r):
    # 왼쪽에 있는 원소
    p = A[l]
    # 앞에서 시작하는 인덱스
    i = l
    # 뒤에서 시작하는 인덱스
    j = r
    # i, j 엇갈리기 전까지
    while i <= j:
        # i번 인덱스에 있는 원소가 p보다 작으면 다음원소 탐색
        while i <= j and A[i] <= p:
            i += 1

        # j번 인덱스에 있는 원소가 p보다 크면다음원소 탐색
        while i <= j and A[j] >= p:
            j -= 1

        # 다 돌고나서도 i가 j보다 작으면
        # p보다 큰 원소가 i번
        # p보다 작은 원소가 j번에 있다.
        # 바꿔 주면 된다.
        if i < j:
            A[i], A[j] = A[j], A[i]

    # i랑 j가 교차
    # 왼쪽에는 기준보다 작은 원소들이 모여있고
    # 오른쪽에는 기준보다 큰 원소들이 모여있음
    # 기준 원소를 그 사이에 끼워넣으면 위치 확정
    A[l], A[j] = A[j], A[l]

    # 기준원소의 위치는 j로 확정
    return j

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    quicksort(li, 0, N - 1)
    print(f"#{tc} {li[N//2]}")