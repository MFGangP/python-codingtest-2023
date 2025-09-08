# 총 10개의 테스트 케이스
for time in range(1, 11):
    # 덤프 횟수
    D = int(input())
    # 각 상자의 높이 값
    box_heights = list(map(int, input().split()))

    # 덤프 횟수만큼 반복
    for i in range(D):
        # 최대 최소 인덱스를 저장할 변수
        max_heights_index = 0
        min_heights_index = 0

        # 최댓값과 최솟값의 인덱스를 찾기.
        for j in range(1, len(box_heights)):
            # 최댓값 인덱스
            if box_heights[j] > box_heights[max_heights_index]:
                max_heights_index = j
            # 최솟값 인덱스
            if box_heights[j] < box_heights[min_heights_index]:
                min_heights_index = j
        
        # 평탄화가 완료되었을 때
        if box_heights[max_heights_index] - box_heights[min_heights_index] <= 1:
            break
        # 평탄화 아직 진행 중일 때
        # 가장 높은 상자에서 가장 낮은 상자로 상자를 이동.
        box_heights[max_heights_index] -= 1
        box_heights[min_heights_index] += 1
    
    # break문 타면 값이 사라지니까 다시 찾아야함.
    max_heights_index = 0
    min_heights_index = 0

    for j in range(1, len(box_heights)):
        if box_heights[j] > box_heights[max_heights_index]:
            max_heights_index = j
        if box_heights[j] < box_heights[min_heights_index]:
            min_heights_index = j
            
    print(f"#{time} {box_heights[max_heights_index] - box_heights[min_heights_index]}")