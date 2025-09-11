import sys
sys.stdin = open("binary_search_input.txt", "r")
sys.stdout = open("binary_search_output.txt", "w")

T = int(input())

def binary_search(target):
    start = 0
    end = N - 1
    # 초기값 : 0, 왼쪽 : 1, 오른쪽 : 2
    direction = 0

    while start <= end:
        mid = (end + start) // 2

        # 값을 찾은 경우
        if A_list[mid] == target:
            return 1
        
        # 왼쪽 탐색할 경우
        elif A_list[mid] > target:
            # 직전 탐색이 왼쪽이였을 경우
            if direction == 1:
                # 종료
                return 0
            # 끝 지점 갱신
            end = mid - 1
            # 방향성 설정
            direction = 1

        # 오른쪽 탐색할 경우
        elif A_list[mid] < target:
            # 직전 탐색이 오른쪽이였을 경우
            if direction == 2:
                # 종료
                return 0
            # 시작 지점 갱신
            start = mid + 1
            # 방향성 설정
            direction = 2
    else:
        return 0
    
for tc in range(1, T+1):
    # A,B 리스트 길이
    N, M = map(int, input().split())
    # 
    result = 0
    # 탐색 대상 리스트
    A_list = list(map(int, input().split()))
    # 탐색해야할 값 리스트
    B_list = list(map(int, input().split()))
    # 이진 탐색은 정렬이 기본 세팅
    A_list.sort()

    # B 리스트 내부 요소로 탐색
    for value in B_list:
        result += binary_search(value)

    print(f"#{tc} {result}")