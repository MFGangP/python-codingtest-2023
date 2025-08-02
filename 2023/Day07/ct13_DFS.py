# 백준 11724 - 연결요소 개수 확인
import sys 
# 재귀호출 파이썬 제한 1000번까지 가능
sys.setrecursionlimit(10 ** 6) # 1000000
# 입력받는 속도가 느리기 때문에, 백준에서 그냥 돌리면 입력오류 발생 가능
input = sys.stdin.readline
# 입력값 두개를 int형으로 받는다. 띄어쓰기 기준
n, m = map(int,input().split())# 6 5
# node 기준 n+1은 앞에 0을 버리겠다는 뜻
A=[[] for _ in range(n+1)] 
# x, 7열 2차원 리스트
visited = [False] * (n+1)
# [0, 1, 2, 3, 4, 5, 6]

# DFE 함수(재귀함수)
def DFS(v):
    visited[v] = True
    # 방문했는지 안했는지 체크하기위한 문장
    for i in A[v]:
        if not visited[i]: # 만약에 v노트에 방문을 안했다면
            DFS(i)

for _ in range(m): # 엣지의 개수만큼 돌면서
    s, e = map(int, input().split())
    A[s].append(e) # 무방향이기 때문에 양쪽에 다 엣지 추가
    A[e].append(s)

count = 0 # 그래프 개수 나타내기

for i in range(1, n+1): # 얘도 0은 버리겠다.
    if not visited[i]: # 연결 노드 중에서 방문하지 않을거만 방문
        count += 1 
        # 엣지 연결이 끊겨있는 나머지 값들이 있을 때 유효
        DFS(i)

print(count)