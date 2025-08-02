# 백준 18352번 - 특정 거리의 도시 찾기

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split()) # 노드 수, 엣지 수, 목표거리, 시작노드

A = [[] for _ in range(N + 1)] # A 초기화
answer = [] # 값 담을 리스트
visited = [-1] * (N + 1)    # 방문 거리 저장 리스트(중첩 할 것이기 때문에)

def BFS(v):
    queue = deque() 
    queue.append(v)
    visited[v] += 1 # -1이 0으로 바뀜
    while queue: # 큐가 있는 동안에, 큐가 비어 있을 때 까지
        now_Node = queue.popleft()
        for i in A[now_Node]: # 
            if visited[i] == -1: # 미방문 일 때
                visited[i] = visited[now_Node] + 1 # 현재 노드값에 +1
                queue.append(i)
                
# 두번 째 줄 부터 엣지 입력
for _ in range(M): # 엣지 개수만큼
    S, E = map(int, input().split())    # 엣지 입력
    A[S].append(E)

BFS(X) # 시작점 부터 BFS 시작

for i in range(N + 1): 
    if visited[i] == K:
        answer.append(i)

if not answer: # 아무거도 없으면 len(answer) == 0
    print(-1)
else: # 뭐라도 있으면
    answer.sort() # 정렬하고
    for i in answer: # 출력
        print(i)
