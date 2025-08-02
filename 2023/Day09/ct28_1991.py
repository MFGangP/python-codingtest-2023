# 백준 1991 - 트리순회
import sys
input = sys.stdin.readline

N = int(input()) # 7
tree = {} # 딕셔너리 형태로 선언

for _ in range(N):
    root, left, right = input().split() # A B C 형태로 받기로 해서 인트 아님
    tree[root] = [left, right]

def preOrder(now): # 전위순회
    if now == '.': return 
    print(now, end='') # 부모노드 출력
    preOrder(tree[now][0]) # 왼쪽 노드 탐색
    preOrder(tree[now][1]) # 오른쪽 노드 탐색

def inOrder(now): # 중위순회
    if now == '.': return
    inOrder(tree[now][0]) # 왼쪽 노드 탐색
    print(now, end='') # 부모노드 출력
    inOrder(tree[now][1]) # 오른쪽 노드 탐색

def postOrder(now): # 후위 순회
    if now == '.': return
    postOrder(tree[now][0]) # 왼쪽 노드 탐색
    postOrder(tree[now][1]) # 오른쪽 노드 탐색
    print(now, end='') # 부모노드 출력

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')