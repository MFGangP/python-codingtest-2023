import sys
sys.stdin = open("binary_input.txt", mode='r')
sys.stdout = open("binary_output.txt", mode='w')

T = int(input())
# a = 찾고자 하는 리스트
# N = 끝 지점
# key = 찾고자 하는 대상
def binarySearch(a, N, key): # key를 찾으면 인덱스, 실패하면 0 반환
    time_value = 0
    start = 0
    end = N-1
    while start <= end:
        time_value += 1
        middle = int((start + end)//2)
        if a[middle] == key: # 검색 성공
            # 검색 횟수 반환
            return time_value
        elif a[middle] > key: # 찾는 값보다 크면
            end = middle # 왼쪽 구간 선택
        else: # 찾는 값보다 작으면
            start = middle # 오른쪽 구간 선택
    return 0 # 검색 실패

for time in range(1, T+1):
    # 테스트 케이스 별로 책의 전체 쪽 수 P, 
    # A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 
    # 1<= P, Pa, Pb <=1000
    P, Pa, Pb = list(map(int, input().split()))

    P_list = []

    for i in range(P):
        P_list.append(i+1)

    A_time = binarySearch(P_list, P, Pa)
    B_time = binarySearch(P_list, P, Pb)

    # B가 이기면
    if A_time < B_time:
        print(f"#{time} A")
    # A가 이기면
    elif A_time > B_time:
        print(f"#{time} B")
    # 비기면
    elif A_time == B_time:
        print(f"#{time} 0")