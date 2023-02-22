# 백준 1717번 - 집합 표현하기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
N, M = map(int, input().split()) # 원소 개수, 질의 개수
parent = [0] * (N + 1) # 0번 안쓸거다. [0 for _ in range(N + 1)]

def find(a):    # find 연산
    if a == parent[a]: # 노드랑 자기 자신 대표 노드가 같다면 
        return a # 노드 리턴
    else: # 같지 않다면
        parent[a] = find(parent[a]) # 대표 노드의 대표 노드 검색, 재귀 호출 -> 경로 압축
        return parent[a] # 찾은 대표노드 리턴

def union(a, b):    # 대표노드 변경 (끼리 합치기)
    a = find(a) # 대표노드 검색
    b = find(b)
    if a != b:  # 두 개가 같지 않다면
        if a < b:
            parent[b] = a
        else:
            parent[a] = b # 작은 값의 대표노드로 변경

def checkSame(a, b):    # 같은지 체크
    a = find(a) # 대표 노드 검색
    b = find(b) 
    if a == b: # 둘이 같다면 True
        return True
    # 둘이 다르다면 False
    return False

for i in range(0, N + 1): # 원소 개수만큼
    parent[i] = i # 자기자신 대표노드로 초기화

for i in range(M): # 질문 개수만큼
    question, a, b = map(int, input().split()) # 0 1 3, 1 1 7
    if question == 0: # 질문 0이면 유니온
        union(a, b)
    else: # 1이면 체크
        if checkSame(a, b):
            print('YER')
        else:
            print('NO')