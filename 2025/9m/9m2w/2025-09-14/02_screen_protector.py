import sys
sys.stdin = open("screen_protector_input.txt", "r")
sys.stdout = open("screen_protector_output.txt", "w")

def check_performance(current_film):
    # 모든 세로 줄에 검사
    for col in range(W):
        col_passed = False # 현재 열이 통과했는지 여부
        max_continuous = 1
        current_continuous = 1
        
        # 각 열을 위에서 아래로(행) 순회
        for row in range(1, D):
            # 이전 셀과 같은 특성이면 연속 카운트 증가
            if current_film[row][col] == current_film[row-1][col]:
                current_continuous += 1
            else: # 다른 특성이면 1로 초기화
                current_continuous = 1
            
            # 현재까지의 최대 연속 길이를 갱신
            max_continuous = max(max_continuous, current_continuous)

        # 해당 열의 최대 연속 길이가 K 이상이면 통과
        if max_continuous >= K:
            col_passed = True
        
        # 만약 통과하지 못한 열이 하나라도 있다면, 즉시 전체 성능 검사 실패
        if not col_passed:
            return False
            
    # 모든 열이 검사를 통과했다면, 전체 성능 검사 성공
    return True
    
# 현재 행, 약품 투입 횟수
def solve(index, count):
    global result

    # 가지치기
    if result <= count:
        return

    # 종료 조건
    if index == D:
        if check_performance(matrix):
            result = min(result, count)
        return
    
    # 재귀
    # 아무거도 안바꾸고 다음으로 넘어감 
    solve(index + 1, count)

    original_array = matrix[index][:]

    # 행 값을 A 타입으로 바꿨을 경우
    matrix[index] = [0] * W
    solve(index + 1, count + 1)
    matrix[index] = original_array

    # 행 값을 B타입으로 바꿨을 경우
    matrix[index] = [1] * W
    solve(index + 1, count + 1)
    matrix[index] = original_array

T = int(input())

for tc in range(1, T+1):
    # D : 세로 크기 (두께)
    # W : 가로 크기 (너비)
    # K : 세로 검사 합격 기준
    D, W, K = map(int, input().split())
    # 0 = A, 1 = B
    matrix = [list(map(int, input().split())) for _ in range(D)]
    # 어차피 늘어나봤자 D
    result = D

    solve(0, 0)
    
    print(f"#{tc} {result}")