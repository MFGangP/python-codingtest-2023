# 초기값 0,0
def make_set(i, j, selected, total):
    global min_value
    # 0. 가지치기 최소 값보다 커졌으면 종료
    if total >= min_value:
        return
 
    # 1. 종료 조건 설정 => 모든 행에서 다 골랐다면
    if i == N:
        if min_value > total:
            min_value = total
        return
     
    # 열 범위 벗어나면 진행x
    if j == N:
        return
 
    # 2. 재귀 호출 - 이 단계에서 다음 단계로 어떻게 진행할거냐
    # j열을 골랐으면 다음 i+1 행으로 (한줄에 하나만 선택 가능) 
    # 단 j열을 고르지 않았어야함
    # 세로, 가로 모두 중복되지 않아야함. N-Queen과 동일한 문제.
    can_j = True
    # 열을 바꿔가면서 j 값을 선택 할 수 있는지 확인하기 위해.
    for k in range(N):
        # k열의 j가 먼저 선택된 값이 있는지 없는지 체크
        if selected[k][j]:
            # 선택된 값이 있으면 j를 선택할 수 없으므로 False로 변경
            can_j = False
            break
    # j 값을 선택할 수 있다면
    if can_j:
        # i,j에 방문 처리하고,
        selected[i][j] = 1
        # 재귀함수 현재 행에서 다음 행으로 진행.
        make_set(i+1, 0, selected, total+array[i][j])
 
    # j열을 안골랐으면 다음 j+1열으로
    selected[i][j] = 0
    make_set(i, j+1, selected, total)
 
T = int(input())
 
for testcase in range(1, T+1):
    # 배열 크기
    N = int(input())
     
    # NxN 배열 입력
    array = [list(map(int, input().split())) for _ in range(N)]
 
    # 양수 무한대 선언
    min_value = float('inf')
     
    # 재귀 함수 시작
    make_set(0, 0, [[0] * N for _ in range(N)], 0)
 
    print(f"#{testcase} {min_value}")