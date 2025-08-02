# 백준 11003 - 최소값 찾기 1
from collections import deque
# from pythonds.basic.deque import Deque
mydeque = deque() # deque 생성
N, L = map(int, input().split()) # 전체 리스트의 크기, 슬라이딩 윈도우 사이즈 
now = list(map(int, input().split())) # 1 5 2 3 6 2 3 7 3 5 2 6

# 새값이 들어올때마다 정렬 대신 현재 수보다 큰 값을 덱에서 제거
# 시간 복잡도를 줄임

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 전체 인덱스에 마지막 값
        # deque 안에있는 값이 지금 들어가는 값 보다 크면
        mydeque.pop() # 기존에 들어있는 큰 값을 빼버린다.
    mydeque.append((now[i], i)) # 지금 값을 추가한다.
    if mydeque[0][1] <= i - L:  
        mydeque.popleft() # 범위를 벗어난 값도 덱 왼쪽에서 뺀다
    print(mydeque[0][0], end=' ') # 이 값은 무조건 최소값(min()과 동일)
