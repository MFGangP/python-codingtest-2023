import sys
sys.stdin = open("palindrome2_input.txt", mode='r')
sys.stdout = open("palindrome2_output.txt", mode='w')

for _ in range(1, 11):
    N = 100
    # M은 문제에서 주어지지 않지만, 코드가 M을 요구하지 않도록 수정합니다.
    time = int(input())
    array = [list(input()) for _ in range(N)]

    palindrome_num = 0

    # 가로 방향 탐색
    for i in range(N):
        for j in range(N):
            # j 부터 끝까지 전부 확인
            for k in range(j, N):
                word = array[i][j:k+1]
                if word == word[::-1]:
                    if palindrome_num < len(word):
                        palindrome_num = len(word)

    # 세로 방향 탐색
    for j in range(N):
        for i in range(N):
            # i 부터 끝까지 전부 확인
            for k in range(i, N):
                word = [array[p][j] for p in range(i, k+1)]
                if word == word[::-1]:
                    if palindrome_num < len(word):
                        palindrome_num = len(word)

    print(f"#{time} {palindrome_num}")