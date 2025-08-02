# 백준 1516번 - 게임 개발하기
from collections import deque

N = int(input()) # 건물 수
A = [[] for _ in range(N+1)] # 건물 데이터 저장 인접 리스트
indegree = [0] * (N + 1)
selfBuild = [0] * (N + 1)
# 진입 차수 리스트 0번 데이터는 안쓴다. 
# 자기 자신을 짓는 시간 저장 리스트
# 똑같다 [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    inputList = list(map(int, input().split())) # 4(자기 건물 시간) 1 3 -1 / 10 -1
    selfBuild[i] = inputList[0] # 건물 빌드 시간
    index = 1
    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1: # while 문 탈출
            break
        A[preTemp].append(i)
        indegree[i] += 1 # 진입차수 증가

queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i) # 1부터 시작

result = [0] * (N+1) 

while queue : # 위상 정렬 수행
    now = queue.popleft()
    for next in A[now]: # 1 -> 2, 3, 4
        indegree[next] -= 1 # 방문했으니까 -1 감소
        # 시간 업데이트
        result[next] = max(result[next], result[now] + selfBuild[now]) 
        if indegree[next] == 0:
            queue.append(next)
        
for i in range(1, N + 1):
    print(result[i] + selfBuild[i])