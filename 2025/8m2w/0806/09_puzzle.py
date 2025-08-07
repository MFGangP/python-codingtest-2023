import sys
sys.stdin = open("sudokuinput.txt", mode='r')
sys.stdout = open("sudokuoutput.txt", mode='w')

T = int(input())

for time in range(1, T + 1):
    N = 9
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 1  
    
    for i in range(N):
        row_set = set()
        col_set = set()
        for j in range(N):
            if matrix[i][j] in row_set:
                result = 0
                break
            row_set.add(matrix[i][j])
            
            if matrix[j][i] in col_set:
                result = 0
                break
            col_set.add(matrix[j][i])
        if result == False:
            break

    # 3x3 블록 검사
    if result == 1:
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                block_set = set()
                for si in range(i, i + 3):
                    for sj in range(j, j + 3):
                        if matrix[si][sj] in block_set:
                            result = 0
                            break
                        block_set.add(matrix[si][sj])
                    if result == 0:
                        break
                if result == 0:
                    break
    print(f"#{time} {result}")