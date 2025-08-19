# NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 
# 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
# 조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
# 예를 들어 다음과 같이 배열이 주어진다.
 
# 2 1 2
# 5 8 5
# 7 2 2

# 이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 
# 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

import sys
sys.stdin = open("array_min_sum_input.txt","r")
sys.stdout = open("array_min_sum_output.txt","w")

def make_set(i, j, selected, min_value):
    if i >= N and j >= N:
        return min_value
        
    # 1. 종료 조건 설정
    if j >= N or i >= N:
        # selected 배열을 보고 내가 어떤 원소를 선택했었는지 확인
        subset = []
        sum = 0
        for i in range(N):
            for j in range(N):
                # 내가 i번 원소를 부분집합에 포함하기로 했었다면
                if selected[i][j]:
                    subset.append(array[i][j])
                    sum += array[i][j]
        # 백트래킹을 안배웠으면 여기서 값 판단을 하고 있었을것
        if min_value > sum:
            min_value = sum
        return

    # 2. 재귀 호출 - 이 단계에서 다음 단계로 어떻게 진행할거냐
    # idx번 원소를 부분 집합에 넣고 idx+1번 원소를 판단하기
    selected[i][j] = 1
    make_set(0, j+1, selected, min_value)
    selected[i][j] = 0
    make_set(i+1, j, selected, min_value)

T = int(input())


for testcase in range(1, T+1):
    # 배열 크기
    N = int(input())
    # NxN 배열 입력
    array = [list(map(int, input().split())) for _ in range(N)]

    min_value = array[0][0] + array[0][1] + array[0][2] 

    make_set(0, 0, [[0] * N for _ in range(N)], min_value)

    print(f"#{testcase} {min_value}")