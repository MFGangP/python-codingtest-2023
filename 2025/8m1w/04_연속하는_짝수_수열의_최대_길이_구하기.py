T = int(input())

longest_evne_list_index = 0

for repeat_time in range(1, T + 1):
    # 제공되는 리스트 총 길이
    list_nums = int(input())
    # 입력받는 리스트 - 띄어쓰기 기준으로 Split
    input_list = list(map(int, input().split()))
    # 긴 짝수 갯수 
    longest_evne_list_index = 0
    evne_index = 0
    # 리스트 갯수만큼 반복
    for i in range(list_nums):
        # 그냥 짝수가 아니라 연속된 짝수 +1
        if input_list[i] % 2 == 0:
            evne_index += 1
            # 가장 긴 인덱스가 연속된 짝수 인덱스 보다 작을 경우 값 변경
            if longest_evne_list_index <= evne_index:
                longest_evne_list_index = evne_index
        # 홀수 나오면 짝수 인덱스 초기화
        else:
            evne_index = 0
        
    print(f"#{repeat_time}", longest_evne_list_index)