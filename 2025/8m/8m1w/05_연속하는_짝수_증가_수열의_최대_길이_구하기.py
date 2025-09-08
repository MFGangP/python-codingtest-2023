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