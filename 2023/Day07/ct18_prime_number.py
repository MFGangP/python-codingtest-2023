# 백준 1929번 소수구하기 
import math
M, N = map(int, input().split())
A = [0] * (N + 1) # 이게 초기화
for i in range(2, N+1):
    A[i] = i # 인덱스 채워넣기

for i in range(2, int(math.sqrt(N))+1): # 제곱근까지만 수행
    if A[i] == 0: 
        continue
    # i = 2 , 4/6/8/10/12....
    # i = 3 , 3/6/9/12/15....
    for j in range(i + i, N + 1, i): # 배수로 지우기
        A[j] = 0

for i in range(M, N + 1):
    if A[i] != 0:
        print(A[i])
