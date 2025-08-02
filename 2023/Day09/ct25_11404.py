# 백준 11404
import sys
input = sys.stdin.readline

N = int(input()) # 도시 개수
M = int(input()) # 노선 개수
distance = [[sys.maxsize for j in range(N + 1)] for i in range(N + 1)] 
# 앞에 값을 넣으면 그 값으로 초기화 된다 - 충분히 큰 값으로 초기화 
# 6X6 인접행렬
for i in range(1, N+1):
    distance[i][i] = 0 # 인접 행렬 자기자신 초기화

for i in range(M):
    s, e, v = map(int, input().split())
    if distance[s][e] > v: # 중복된 노선 중 더 저렴한 버스가 있으면
        distance[s][e] = v

# 플로이드 워셜 시작
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 경유지를 경유해서 오는 값이 이전 경로 값보다 작을 경우
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()