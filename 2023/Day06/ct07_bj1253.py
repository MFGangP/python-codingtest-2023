import sys
input = sys.stdin.readline
N = int(input()) # 몇개 입력할껀지
Result = 0 # 변수 초기화
A = list(map(int, input().split())) # 한 줄에 입력 다 받을 때
A.sort() # 그냥 정렬

for k in range(N):
    find = A[k] # 찾을 수 지정
    i = 0; j = N - 1 # i는 리스트 첫번째, j는 리스트 마지막 번 째 위치
    while i < j:    # 두 인덱스가 만나면 반복 종료
        if A[i] + A[j] == find: # 두 수의 합이 찾는 수와 일치
            if i != k and j != k:   # i와 j는 k와 같은 위치가 되면 안됨
                Result += 1
                break
            elif i == k: 
                i += 1 #                
            elif j == k: 
                j -= 1 # 
        elif A[i] + A[j] < find: # i를 증가시켜야 합의 수가 커짐
            i += 1
        elif A[i] + A[j] > find:   # j를 감소시켜야 합의 수가 작아짐
            j -= 1
print(Result)    
