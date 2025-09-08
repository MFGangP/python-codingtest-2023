repeat_time = 0
for time in range(1, 11):
    # 테스트 리스트 갯수
    building_count = int(input())

    # 나보다 최소 1이 작은 건물이 2칸 이상 떨어져있으면 조망권 확보

    # 건물 크기가 비교 대상보다 작거나 없어거나
    # 이동 거리가 2칸 이상이면 된다.

    # 건물 크기 입력 받기
    # 최대 조망권 확보 세대 수
    max_view = 0
    # 맨 왼쪽, 오른쪽 두칸은 0으로 고정
    input_list = list(map(int, input().split()))
    repeat_time += 1

    # 건물 갯수 만큼 반복 3번째 부터 끝에서 -3번 까지
    for i in range(2, building_count-2):
        # 비교 대상 건물
        current_building_height = input_list[i]
        # 앞 뒤 건물 중 가장 높은 건물
        max_building_height = 0
        # 맨 왼쪽, 오른쪽 두칸은 0으로 고정
        # i 번째 건물의 -2번에서 2번 건물 까지 반복
        for j in range(i-2, i+3):
            # 값을 비교하는게 아니라 인덱스를 비교 해야한다.
            # 만약 자기 자신과 비교하게 된다면
            if i == j:
                # 비교 할 필요가 없기 때문에 넘긴다.
                continue
            elif max_building_height < input_list[j]:
                # 최대 값을 교체.
                max_building_height = input_list[j]
        # 현재 내 빌딩이 추가하려는 빌딩보다 클 경우에만 추가 가능
        if current_building_height > max_building_height:
            # 조망권 - 현재 빌딩에서 비교 대상 건물 층 수를 뺀 나머지 값 추가.
            max_view += input_list[i] - max_building_height

    print(f"#{time} {max_view}")