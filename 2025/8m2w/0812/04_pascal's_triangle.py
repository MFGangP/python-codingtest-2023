import sys
sys.stdin = open("pascals_triangle_input.txt", mode='r')
sys.stdout = open("pascals_triangle_output.txt", mode='w') 

def pascals_triangle(N, array):
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                array[i][j] = 1
            else:
                # 파스칼 수는 자신의 왼쪽과 오른쪽 위의 숫자를 더해서 낸다.
                array[i][j] = array[i-1][j-1] + array[i-1][j]
        print(*array[i])

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    # N x N 배열 선언
    array = [[0] * i for i in range(1, N+1)]

    print(f"#{testcase}")
    pascals_triangle(N, array)