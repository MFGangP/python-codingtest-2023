# import sys
# sys.stdin = open("sp_arr_input.txt", mode='r')
# sys.stdout = open("sp_arr_output.txt", mode='w')

T = int(input())

# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 
# 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 
# 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 
# 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.

# 10 1 9 2 8 3 7 4 6 5

# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 
# 10<=N<=100, 1<=ai<=100

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 
# 특별히 정렬된 숫자를 10개까지 출력한다.

def selection_sort(num_lists, N):
    for i in range(0, 10): # 정렬 구간의 시작 인덱스
        idx = i # 첫 원소를 최대로 가정
        # 홀수 인덱스 - 최대 값 순
        if i % 2 != 0:
            # 홀수 인덱스 계산하고 나면 짝수 인덱스로 넘겨야함
            for j in range(i+1, N):
                if num_lists[idx] > num_lists[j]:
                    idx = j
            num_lists[i], num_lists[idx] = num_lists[idx], num_lists[i] # 구간 최솟값을 구간 맨 앞으로
        # 짝수 인덱스 - 최소 값 순 
        if i % 2 == 0:
            # 짝수 인덱스 계산하고 나면 홀수 인덱스로 넘겨야함
            for j in range(i+1, N):
                if num_lists[idx] < num_lists[j]:
                    idx = j
            num_lists[i], num_lists[idx] = num_lists[idx], num_lists[i] # 구간 최솟값을 구간 맨 앞으로
        
for time in range(1, T+1):
    
    N = int(input())
    num_lists = list(map(int, input().split()))

    new_num_lists = selection_sort(num_lists, N)
    print(f"#{time}",*num_lists[:10])
