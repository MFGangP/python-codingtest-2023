answer = 0
A = list(map(str,input().split('-'))) # - 기준으로 잘라서 문자열 리스트

def mySum(i):   # - 로 나눈 각 수식 문자열 합 구하기 함수
    A_sum = 0
    tmp = str(i).split('+') # + 기준으로 수식 자름
    
    for k in tmp:   # k 는 문자열
        A_sum += int(k) # '78' 같은 문자열이므로 int()
    return A_sum

for i in range(len(A)):
    temp = mySum(A[i])

    if i == 0:
        answer += temp  # 맨 처음 값
    else:
        answer -= temp  # 나머지 값

print(answer)