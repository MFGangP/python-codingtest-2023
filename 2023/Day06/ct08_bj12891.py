checkList = [0] * 4 # ACGT 유전자 값
myList = [0] * 4 # 부분 문자열의 ACGT 개수
checkSecret = 0 # 내가 찾고자 했던 문자를 찾은 횟수 담는 변수

def myadd(c): # 새로 들어온 문자를 처리
    global checkList, myList, checkSecret
    if c == 'A': # 만나는 놈이 A면 myList내 
        myList[0] += 1 # A 개수에 해당하는 0번째 칸 값 1증가 시키고 
        if myList[0] == checkList[0]: # 내가 요구하는 (조건을 충족했으면) 개수만큼 찾았으면 
            checkSecret += 1    # 체크리스트 값 1증가
    elif c == 'C':  # C면 myList내 C에 해당하는 개수 1개 증가
        myList[1] += 1 # C 개수에 해당하는 1번째 칸 값 1증가 시키고 
        if myList[1] == checkList[1]: # 내가 요구하는 (조건을 충족했으면) 개수만큼 찾았으면
            checkSecret += 1    # 체크리스트 값 1증가
    elif c == 'G': # G면 myList내 G에 해당하는 개수 1개 증가
        myList[2] += 1  # G 개수에 해당하는 1번째 칸 값 1증가 시키고
        if myList[2] == checkList[2]: # 내가 요구하는 (조건을 충족했으면) 개수만큼 찾았으면
            checkSecret += 1    # 체크리스트 값 1증가
    elif c == 'T': # T면 myList내 T에 해당하는 개수 1개 증가
        myList[3] += 1  # T 개수에 해당하는 1번째 칸 값 1증가 시키고
        if myList[3] == checkList[3]:# 내가 요구하는 (조건을 충족했으면) 개수만큼 찾았으면
            checkSecret += 1    # 체크리스트 값 1증가

def myremove(c): # 제거되는 문자를 처리
    global checkList, myList, checkSecret
    if c == 'A': # 찾는 애는 A
        if myList[0] == checkList[0]: 
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
# S = 살펴봐야하는 문자열의 길이, P = 지정해서 봐야할 문자열 길이
Result = 0
A = list(input())
checkList = list(map(int, input().split())) # 문자열에서 내가 요구하는 글자 최소 개수

for i in range(4): # 4번 반복
    if checkList[i] == 0:   # A,C,G,T가 들어있으면 무조건 1증가
        checkSecret += 1 # 없어도 되는 애들은 거름

for i in range(P): # 부분 문자열 갯수만큼
    myadd(A[i]) 

if checkSecret == 4:  # 4 = 네자리 유전자 글자 A,C,G,T 모두 만족
    Result += 1 # 결과에 1 더해준다.

# S = 살펴봐야하는 문자열의 길이, P = 지정해서 봐야할 문자열 길이
for i in range(P, S): # EX) 2, 4  4개짜리 문자열에서 2개씩 살펴보기 
    j = i - P # 0 - 2 = -2
    myadd(A[i]) # 이번 슬라이드에서 처리된 값을 추가
    myremove(A[j])  # 이전 슬라이드에서 처리한 값을 제거
    if checkSecret == 4: # 싹다 돌았더니 찾는 값 4개가 충족됐다
        Result += 1 # 그럼 결과에 1을 더해준다.

print(Result)   # 몇개나 찾았는지 값 표시