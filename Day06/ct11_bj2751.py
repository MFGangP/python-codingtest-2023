# 백준 수 정렬하기2 2751
# 1조개 처리 0(n^2)는 불가
import sys
input = sys.stdin.readline
print = sys.stdout.write
# s = 시작지점 , e = 종료지점
def merge_sort(s, e): # 병합 정렬
    if e - s < 1: return # 종료 지점에서 시작지점을 뺀게 1보다 작으면 끝
    m = int(s + (e - s) / 2) # m(중간점) 구하는 식
    merge_sort(s, m) # 시작점에서 중간점 까지 
    merge_sort(m + 1, e) # 중간점에서 종료점 까지
    for i in range(s, e + 1): 
        # 시작점에서 끝지점 + 1(중간점 2번 들어가니까)원소만큼 반복
        tmp[i] = A[i] # 임시 리스트에 값 저장
    k = s # k는 시작점
    index1 = s # 앞쪽 그룹 시작점
    index2 = m + 1 # 뒷쪽 그룹 시작점

    while index1 <= m and index2 <= e:  # 두 그룹을 병합
        if tmp[index1] > tmp[index2]: # 앞쪽 그룹 시작점이 중간값 보다 크다면
            A[k] = tmp[index2] # 중간점 값을 A리스트 k 번째에 넣고
            k += 1 # A리스트 인덱스를 1 늘리고
            index2 += 1 # 중간점 값을 1 늘린다.
        else: # 중간점 값이 시작점 값 보다 크다면
            A[k] = tmp[index1] # 시작점 값을 A리스트 k 번째에 넣고
            k += 1 # A리스트 인덱스를 1 늘리고
            index1 += 1 # 시작점 값을 1 늘린다.
    # 시작점 ~ 중간점
    while index1 <= m: # 앞쪽 그룹 시작점이 중간값보다 작은 동안
        A[k] = tmp[index1] # A리스트 값에 tmp리스트 값을 넣고
        k += 1 # k 인덱스 값을 1 늘린다.
        index1 += 1 # 앞쪽 그룹 시작점도 1 늘린다.
    # 중간점 ~ 종료점
    while index2 <= e: # 뒷쪽 그룹 시작점이 종료값보다 작은 동안
        A[k] = tmp[index2] # A리스트 값에 tmp리스트 값을 넣고
        k += 1 # k 인덱스 값을 1 늘린다.
        index2 += 1 # 뒷쪽 그룹 시작점도 1 늘린다.

N = int(input()) # 정렬할 수 개수
A = [0] * int(N+1)  # 정렬한 리스트 선언
tmp = [0] * int(N+1) # 정렬할 때 잠시 사용할 임시 리스트 선언

for i in range(1, N+1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N+1):
    print(str(A[i])+'\n')