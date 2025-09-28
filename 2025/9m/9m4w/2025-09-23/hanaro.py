# 환경 부담금 E * L^2 최소로 지불하며,
# N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계
import sys
from heapq import heappop, heappush

sys.stdin = open("hanaro_input.txt", "r")

def prim(start):
    heap = []
    # 가중치, 시작 지점
    heappush(heap, (0, start))

    visited = [0] * N
    # 최소 가중치
    min_w = 0

    while heap:
        w, v = heappop(heap)
        # 
        if min_w < w:
            continue

            
# IM 수준 1문제, A형 수준 1문제
# 파리 퇴치, 1959. 두 개의 숫자열, solvingclub 추가문제 태양열에너지
# DFS, BFS, MST, Dijkstra
# 간단히 설명할 수 있도록 정리.
# 그림으로 이해하기.
# 실습 문제 풀어보기.


T = int(input())

for tc in range(1, T+1):
    # 섬의 개수
    N = int(input())
    
    # x 좌표 리스트
    x_list = list(map(int, input().split()))
    # y 좌표 리스트
    y_list = list(map(int, input().split()))

    # 환경 계수
    E = float(input())

    result = prim(0)

    print(f"#{tc} {result}")