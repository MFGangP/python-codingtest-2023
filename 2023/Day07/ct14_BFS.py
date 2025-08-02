# 백준 1260 - 연결요소 개수 확인
from collections import deque
n, m, Start = map(int,input().split())# 6 5
# node 기준 n+1은 앞에 0을 버리겠다는 뜻
A=[[] for _ in range(n+1)] # 인접리스트

for _ in range(m): # 엣지의 개수만큼 돌면서
    s, e = map(int, input().split())
    A[s].append(e) # 무방향이기 때문에 양쪽에 다 엣지 추가
    A[e].append(s)
# DFE 함수(재귀함수)

for i in range(n+1): # 번호가 작은 노드부터
    A[i].sort() # 방문하기 위해 정렬

# DFS 함수의 정의
def DFS(v):
    print(v, end=' ')
    visited[v] = True
    # 방문했는지 안했는지 체크하기위한 문장
    for i in A[v]:
        if not visited[i]: # 만약에 v노트에 방문을 안했다면
            DFS(i)

# BFS 함수 정의
def BFS(v): 
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue: # queue.empty() != True
        now_Node = queue.popleft() # queue.get()
        print(now_Node, end=' ')
        for i in A[now_Node]:
            if not visited[i]: # 방문한 노드가 아니면
                visited[i] = True # 방문기록 True로 만들어주고
                queue.append(i) 

# 방문기록 초기화
visited = [False] * (n+1)
# DFS 실행
DFS(Start)
print()
# 방문기록 초기화
visited = [False] * (n + 1) 
# BFS 실행
BFS(Start)