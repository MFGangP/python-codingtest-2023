import sys
sys.stdin = open("carrot_input.txt", mode='r')
sys.stdout = open("carrot_output.txt", mode='w')

T = int(input())

# 최소 차이 저장.
min_diff = float('inf')

def dfs(carrot_types_list, index, box1, box2, box3):
    global min_diff

    # 현재 상자 개수 차이가 이미 최소 차이보다 크면 중단
    current_diff = max(box1, box2, box3) - min(box1, box2, box3)
    if index > 0 and current_diff >= min_diff:
        return

    # 기저 사례
    if index == len(carrot_types_list):
        if box1 > 0 and box2 > 0 and box3 > 0:
            if current_diff < min_diff:
                min_diff = current_diff
        return

    # 현재 당근 종류의 개수를 가져옴.
    current_carrot_count = carrot_types_list[index][1]
    
    # 재귀 단계: 현재 당근 그룹을 세 개의 상자에 각각 넣어보고 다음으로.
    dfs(carrot_types_list, index + 1, box1 + current_carrot_count, box2, box3) # box1에 넣기
    dfs(carrot_types_list, index + 1, box1, box2 + current_carrot_count, box3) # box2에 넣기
    dfs(carrot_types_list, index + 1, box1, box2, box3 + current_carrot_count) # box3에 넣기

# 이 문제는 대략적으로 이해하겠는데 구현하라고 하면 못하겠음.
for testcase in range(1, T + 1):
    N = int(input())
    Ci = list(map(int, input().split()))
    
    # 당근을 크기별로 정리.
    carrot_count_dict = {}
    for carrot in Ci:
        carrot_count_dict[carrot] = carrot_count_dict.get(carrot, 0) + 1
    
    # 딕셔너리를 튜플 리스트로 변환하여 순서를 부여.
    carrot_types_list = list(carrot_count_dict.items())
    
    # 만약 당근 종류가 3개 미만이면 포장 불가능.
    if len(carrot_types_list) < 3:
        result = -1
    else:
        # 각 테스트 케이스마다 최소 차이를 초기화.
        min_diff = float('inf')
        # 재귀 함수를 호출하여 탐색을 시작.
        dfs(carrot_types_list, 0, 0, 0, 0)
        # 만약 min_diff가 업데이트되지 않았으면 -1 (포장 불가능)을 반환.
        result = min_diff if min_diff != float('inf') else -1

    print(f"#{testcase} {result}")