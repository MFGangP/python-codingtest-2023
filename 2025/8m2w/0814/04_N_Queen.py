import sys
sys.stdin = open("N_queen_input.txt", mode='r')
sys.stdout = open("N_queen_output.txt", mode='w') 

def solve(row):
    global result
    
    if row == N:
        result += 1
        return
    # 이해가 안되서 4x4 체스칸 그려서 확인했다
    # 다시 봐도 이해 안되면 그려봐라 머리로 계산 해봐야 이해 안된다.
    for col in range(N):
        # 같은 열에 퀸이 없거나
        # 대각선에 퀸이 없는 경우
        # 좌상 우하, 좌하 우상
        if not is_col[col] and not is_diag1[row + col] and not is_diag2[row - col + N - 1]:
            # 둘 수 있으니까 퀸을 둔 자리 기준 열 대각선 값 True로 변경        
            is_col[col] = True
            is_diag1[row + col] = True
            is_diag2[row - col + N - 1] = True
            # 다음 행에 퀸 두기
            solve(row + 1)
    
            is_col[col] = False
            is_diag1[row + col] = False
            is_diag2[row - col + N - 1] = False

# 전역 변수 선언 (함수 바깥에 위치)
# 체스 말을 두었을 때 열 값 - 어차피 못놓음
is_col = []
# 좌상 우하 - 왼쪽 아래 부분 부터 값을 잰다. 
is_diag1 = []
# 좌하 우상 - 0,0 에서 부터 대각선을 잰다.
is_diag2 = []
N = 0
result = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    # 각 테스트 케이스마다 배열 초기화
    is_col = [False] * N
    # 좌상 우하
    is_diag1 = [False] * (2 * N - 1)
    # 좌하 우상
    is_diag2 = [False] * (2 * N - 1)

    result = 0

    solve(0)
    print(f"#{test_case} {result}")