# 백준 11725 리프 노드의 개수 구하기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input()) # 7
visited = [False] * (N + 1) # 방문기록
tree = [[] for _ in range(N+1)] # 트리
answer = [0] * (N + 1) # 정답 리스트

for _ in range(1, N):
    n1, n2 = map(int, input().split()) # 부모 자식 노드 입력 순서 X
    tree[n1].append(n2)
    tree[n2].append(n1)

# DFS 탐색
def DFS(number):
    visited[number] = True # 방문
    for i in tree[number]:
        if not visited[i]:
            answer[i] += number # 부모 노드를 정답 리스트에 저장
            DFS(i)

DFS(1) # 부모 노드로 부터 DFS 시작

for i in range(2, N+1): # 1번은 루트노드니까 부모 없음
    print(answer[i])