import sys
sys.stdin = open("elec_cart_input.txt", "r")
sys.stdout = open("elec_cart_output.txt", "w")

T = int(input())

# 중복되지 않는 순서 리스트 출력
def non_duplication_permutation(T: int, permutation_array: list):
    global result
    # 리스트에 값이 있고 첫번째 값이 0이고
    # 리스트 길이가 최대 길이라면
    if permutation_array and permutation_array[0] == 0 and len(permutation_array) == N:
        permutation = permutation_array[:]
        permutation.append(0)
        p = permutation[:len(permutation)-1]
        q = permutation[1:len(permutation)]

        total = 0
        for i in range(len(p)):
            total += matrix[p[i]][q[i]]

        # 계산 완료 되었을 때
        if result > total:
            result = total     
        return

    for i in range(N):
        if visited[i] == True:
            continue
        visited[i] = True
        permutation_array.append(i)
        non_duplication_permutation(i+1, permutation_array)
        permutation_array.pop()
        visited[i] = False

for tc in range(1, T+1):
    # 배열 크기 입력 받기
    N = int(input())

    result = float("inf")

    # 방문 기록 배열 생성
    visited = [False for _ in range(N+1)]
    # NxN 공배열 선언
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 순열 제작
    non_duplication_permutation(0, [])
    
    print(f"#{tc} {result}")