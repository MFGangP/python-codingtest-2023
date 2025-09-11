import sys
sys.stdin = open("merge_sort_input.txt", "r")
sys.stdout = open("merge_sort_output.txt", "w")

T = int(input())

def merge_sort(start, end):
    if start == end - 1:
        return start, end

    mid = (start + end) // 2
    left_s, left_e = merge_sort(start, mid)
    right_s, right_e = merge_sort(mid, end)

    merge(left_s, left_e, right_s, right_e)

    return start, end

# 범위 안에 있는 값 합치기 
def merge(left_s, left_e, right_s, right_e):
    global right_first

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    if A[left_e - 1] > A[right_e - 1]:
        right_first += 1

    # 왼쪽에서 제일 작은 값 
    l = left_s
    r = right_s
    # 배열의 길이
    N = right_e - left_s
    
    result = [0] * N

    # result의 위치를 가리키는 인덱스
    index = 0
    
    # 합치기 시작
    # 왼쪽에서 작은 값, 오른쪽에서 작은 값
    # 둘 중 작은거 선택해서 result의 index 위치에 놓기
    while l < left_e and r < right_e:
        if A[l] <= A[r]:
            result[index] = A[l]
            l += 1
            index += 1
        else:
            result[index] = A[r]
            r += 1
            index += 1

    # 왼쪽, 오른쪽 한 부분만 많이 남은 경우
    while r < right_e:
        result[index] = A[r]
        r += 1
        index += 1
    
    while l < left_e:
        result[index] = A[l]
        l += 1
        index += 1

    # 새로만든 리스트 원본에 반영
    for i in range(N):
        A[left_s + i] = result[i]

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    right_first = 0

    merge_sort(0, N)

    print(f"#{tc} {A[N//2]} {right_first}")