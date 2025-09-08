import sys
sys.stdin = open("palindrome_input.txt", mode='r')
sys.stdout = open("palindrome_output.txt", mode='w')

for time in range(1, 11):
    # 글자의 수 N이 N개 주어짐
    N = 8 
    M = int(input())
    # N x N 배열
    array = [list(input()) for _ in range(N)]
    # 회문 개수
    palindrome_count = 0

    for i in range(N):
        # 글자 수에 맞게 범위를 지정 해준다.
        # N-M+1 까지 
        for j in range(N-M+1):
            # M 길이의 word 
            word = array[i][j:j+M]
            # 리버스 된 단어와 같다면
            if word == word[::-1]:
                palindrome_count += 1
    # 행으로 확인할 때는 j가 고정되어있어야 한다.
    for j in range(N): 
        # 글자 수에 맞게 범위를 지정 해준다.
        # N-M+1 까지 
        for i in range(N-M+1):
            # 세로로 확인을 해야 하기때문에 i부터 단어길이 M 까지
            word = [array[k][j] for k in range(i, i+M)]
            if word == word[::-1]:
                palindrome_count += 1

    print(f"#{time} {palindrome_count}")