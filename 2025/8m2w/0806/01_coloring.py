T = int(input())

red = 1
blue = 2

for time in range(1, T+1):
    matrix = [[0] * 10 for _ in range(10)]
    count_puple = 0
    # N은 칠 할 개수
    N = int(input())
    for i in range(N):
        # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color
        r1, c1, r2, c2, color = list(map(int, input().split())) 
        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                if color == 1:
                    matrix[x][y] += 1
                elif color == 2:
                    matrix[x][y] += 2
                if matrix[x][y] == 3:
                    count_puple += 1
    print(f"#{time} {count_puple}")
    
