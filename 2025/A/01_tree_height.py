import sys

# 테스트 케이스 수 입력
T = int(input().strip())

# 각 테스트 케이스를 처리하는 반복문
for tc in range(1, T + 1):
    N = int(input().strip())
    h = list(map(int, input().split()))
    
    # ----------------------------------------------------
    # 최소 날짜를 찾는 핵심 함수 (이분 탐색)
    # ----------------------------------------------------
    def min_days_to_target(h, target):
        # 각 나무가 목표 높이에 도달하기 위해 필요한 성장량
        diff = [target - x for x in h]
        
        # 총 필요한 성장량과 1cm, 2cm 물주기 횟수 계산
        S = sum(diff) 
        ones = sum(d & 1 for d in diff)   # 각 나무가 홀수 cm 자라야 하는 횟수 (1cm 물주기 횟수)
        twos = sum(d >> 1 for d in diff)  # 각 나무가 짝수 cm 자라야 하는 횟수 (2cm 물주기 횟수)
    
        # 이분 탐색 범위 설정
        lo, hi = 0, 2 * S + 5  # 최소 날짜는 0, 최악의 경우(1cm씩만)보다 충분히 크게 설정
        ans = hi
    
        # 주어진 날짜(D) 안에 모든 성장을 완료할 수 있는지 판별하는 함수
        def ok(D):
            O = (D + 1) // 2  # D일 중 1cm 성장 물주기가 가능한 날(홀수 날)의 수
            E = D // 2        # D일 중 2cm 성장 물주기가 가능한 날(짝수 날)의 수
            
            # 짝수 날이 부족할 경우, 남은 2cm 성장을 1cm 물주기 두 번으로 대체해야 함
            need_odd = ones + 2 * max(0, twos - E)
            
            # 필요한 1cm 물주기 횟수를 감당할 수 있는지 반환
            return O >= need_odd
    
        # 이분 탐색 시작
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid  # 조건을 만족하므로, 더 작은 날짜를 찾아봄
                hi = mid - 1
            else:
                lo = mid + 1 # 조건을 만족하지 못하므로, 더 큰 날짜를 찾아봄
        return ans

    # ----------------------------------------------------
    # 메인 로직
    # ----------------------------------------------------
    mx = max(h)
    
    # 목표 높이 mx와 mx+1 두 경우를 모두 탐색하여 더 작은 값 채택
    # 홀수 날과 짝수 날의 효율성 때문에 목표 높이의 홀짝에 따라 최적의 답이 달라질 수 있음
    ans = min(min_days_to_target(h, mx), min_days_to_target(h, mx + 1))
    
    print(f"#{tc} {ans}")