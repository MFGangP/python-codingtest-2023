# 2차원 구간 합
# 백준 - 11660
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
# 2차원 행렬 크기, 질의 갯수
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]
# 각 라인 첫번 째 줄은 사용 안하겠다. (0,a) (b,0) 
# for 문 안에 _ 는 아무거도 안하겠다.
# 2차원 배열 만듦
for i in range(n):  # 처음 입력했던 n 번만큼 반복
    # rows에 int 형태로 숫자를 받아서 리스트로 저장한다.
    rows = list(map(int, input().split()))
    # A_row는 (x, y) 행렬
    A_row = [0] + rows
    # A에 0번째 행렬을 제외하고 (x, y)짜리 행렬을 추가한다.
    A.append(A_row)

# 2차원 합배열 D 만듦 O(1024X1024) 백만
for i in range(1, n + 1):   # n - 1 까지 반복하니까 +1 해줘야 한다.
    for j in range(1, n + 1):   # 얘도 마찬가지
        # 구간 합 식
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간합
# _ == m만큼 반복은 하는데 _에 들어가는 수(변수 0, 1, 2..)는 쓰지 않겠다.
for _ in range(m):  # 맨처음 받은 m번 만큼 횟수 반복
    x1, y1, x2, y2 = map(int, input().split()) # x, y를 받아서 구간합 구하는데 쓰겠다.
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)   # 결과 표기