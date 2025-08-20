import sys
sys.stdin = open("ball_and_box_input.txt", mode='r')
sys.stdout = open("ball_and_box_output.txt", mode='w') 

T = int(input())

carrot_dict = {}

def find_carrot(carrot_dict: dict, index, small, middle, big):
    global min_dif_value
    
    current_carrot_count = carrot_types_list[index][1]
    # 0. 백트래킹 조건 설정
    current_count = [small, middle, big]

    # 1. 재귀 함수 탈출 조건 설정
    # 모든 당근을 상자에 넣었을 때
    if index == len(carrot_types_list):
        if small > 0 and middle > 0 and big > 0:
            current_count = max(small, middle, big) - min(small, middle, big)
    # 2. 재귀 함수 진입 조건 설정

for testcase in range(1, T+1):
    # 양수 무한대 값
    min_dif_value = float('inf')
    # 당근 개수
    N = int(input())
    # N개의 당근 크기 리스트
    Ci = list(map(int, input().split()))
    # 당근 크기별로 딕셔너리에 정리
    for carrot in Ci:
        carrot_dict[carrot] = carrot_dict.get(carrot, 0) + 1

    carrot_types_list = list(carrot_dict.items())