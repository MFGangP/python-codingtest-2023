# N개의 양의 정수로 이루어진 수열이 주어질때, 그 수열 안에는 연속하며 증가하는 짝수만으로 이루어진 부분 수열이 존재한다.

# 예를들어 주어진 수열이 2 4 6 8 10 라면
# 이 안에 연속하며 증가하는 짝수만으로 이루어진 부분 수열은 2 4, 6 8 10, 8 10 등이 있다.
# 하지만 이 중에 가장 긴 연속하며 증가하는 짝수 부분 수열은 2 4 6 8 10 이고, 길이는 5이다.

# 예를들어 주어진 수열이 2 2 2 2 2 라면
# 이 안에 연속하며 증가하는 짝수만으로 이루어진 부분 수열은 2 밖에 없다. 따라서 최대 길이는 1이다.

# 연속하며 증가하는 짝수만으로 이루어진 부분 수열 중 가장 긴 길이가 얼마인지 구하는 프로그램을 작성하세요.

# 첫 줄에 테스트케이스의 개수 T가 입력으로 주어집니다.

# 이후엔 각 테스트케이스의 입력이 차례대로 주어지고,
# 각 테스트 케이스의 첫 줄에는 정수의 개수 N이 주어집니다.
# 두 번째 줄에는 N개의 양의 정수로 이루어진 수열이 주어집니다.

# 출력은 예시를 참고하세요. 
 
# 입력
# 4
# 5
# 2 4 6 8 10
# 5
# 2 2 2 2 2
# 5
# 1 3 5 7 9
# 9
# 8 6 9 2 4 6 8 10 12

# 출력
# #1 4
# #2 5
# #3 0
# #4 6

T = int(input())

for repeat_time in range(1, T + 1):
    # 제공되는 리스트 총 길이
    list_nums = int(input())
    # 입력받는 리스트 - 띄어쓰기 기준으로 Split
    input_list = list(map(int, input().split()))
    # 역대 가장 긴 짝수 갯수
    longest_even_list_index = 0
    # 현재 가장 긴 짝수 갯수
    even_index = 0
    # 이전 짝수 값 초기화
    before_even_value = 0
    # 리스트 갯수만큼 반복
    for i in range(list_nums):
        # 짝수인지 확인
        if input_list[i] % 2 == 0:
            # 이전 짝수 값 보다 클 경우 연속된 짝수 갯수 늘리고 값 변경
            if before_even_value < input_list[i]:
                even_index += 1
                # 이걸 왜 1로 바꿈? 정신차려
                before_even_value = input_list[i]
            # 이전 값보다 작은 경우 : 현재 가장 긴 짝수 갯수, 이전 짝수 값 초기화
            elif before_even_value >= input_list[i]:
                even_index = 1
                before_even_value = input_list[i]
            # 현재 가장 긴 짝수 갯수가 역대 가장 긴 짝수 갯수 보다 작을 경우 값 변경
            if longest_even_list_index < even_index:
                longest_even_list_index = even_index
        # 홀수 나오면 짝수 인덱스 초기화
        else:
            even_index = 0
        
    print(f"#{repeat_time}", longest_even_list_index)