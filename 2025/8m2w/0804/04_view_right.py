for repeat_time in range(1, 11):
    # 건물의 개수
    N = int(input())
    input_list = list(map(int, input().split()))

    # 조망권이 확보된 총 층 수를 저장할 변수
    total_view = 0

    # 양쪽 끝 두 칸을 제외하고 건물들을 순회합니다.
    for i in range(2, N - 2):
        # 현재 건물의 높이
        current_building_height = input_list[i]

        # 주변 4개 건물 중 가장 높은 건물의 높이를 찾기 위한 변수
        max_around_height = 0

        # 주변 4개 건물 중 최댓값 찾기.
        if input_list[i - 2] > max_around_height: # -2
            max_around_height = input_list[i - 2]
        if input_list[i - 1] > max_around_height: # -1
            max_around_height = input_list[i - 1]
        if input_list[i + 1] > max_around_height: # 1
            max_around_height = input_list[i + 1]
        if input_list[i + 2] > max_around_height: # 2
            max_around_height = input_list[i + 2]

        # 현재 건물이 주변에서 가장 높은 건물보다 높으면
        if current_building_height > max_around_height:
            # 그 차이만큼 조망권 확보 층수 더하기
            total_view += current_building_height - max_around_height

    print(f"#{repeat_time} {total_view}")
