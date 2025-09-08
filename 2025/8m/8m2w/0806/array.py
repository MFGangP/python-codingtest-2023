N, M = map(int, input().split()) # 모든 문제에서 N, M 을 순서대로 주는게 아니다 주의!
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0

for i in range(N):
	for j in range(M):
		s += (arr[i][j + (M-1-2*j) * (i%2)])
        
#3 4
#1 7 2 8
#6 2 9 3
#5 7 4 2