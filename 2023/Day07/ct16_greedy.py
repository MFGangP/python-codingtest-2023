N, K = map(int, input().split()) # 동전 개수, 목표 금액
A = [0] * N # 동전 데이터 리스트

for i in range(N):  # 리스트 저장
    A[i] = int(input()) 

count = 0 # 누적 동전수 선언

for i in range(N-1, -1, -1): # 역순으로
    if A[i] <= K :  # 현재 동전의 가치가 목표 금액보다 작거나 같으면
        count += K // A[i] # 누적 동전 수 = 목표 금액 / 현재 동전 가치
        K = K % A[i] # 목표 금액 = 목표 금액 % 현재 동전 가치

print(count) # 누적된 동전 수 출력
