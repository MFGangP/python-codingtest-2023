import sys
sys.stdin = open("pascal_input.txt", "r")
sys.stdout = open("pascal_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    pascal = int(input())

    matrix = [[0] * pascal for _ in range(pascal)]

    print(f"#{testcase}")
    for i in range(pascal):
        for j in range(pascal):
            if (i == 0 and j == 0) or j == i:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j] 

            if matrix[i][j] > 0:
                print(matrix[i][j], end=" ")
        print()

            
