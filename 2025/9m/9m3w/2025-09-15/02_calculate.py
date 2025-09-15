from collections import deque
import sys

sys.stdin = open("calculate_input.txt", "r")
sys.stdout = open("calculate_output.txt", "w")

def bfs(start, end):
    # 1. 큐와 visited 배열(또는 set)을 준비합니다.
    # 문제의 최대값이 1,000,000이므로 visited 배열 크기를 넉넉하게 잡습니다.
    visited = [False] * 1000001
    
    # 2. 시작점을 큐에 넣습니다. 상태는 (현재 숫자, 현재까지의 연산 횟수) 입니다.
    queue = deque([(start, 0)])
    
    # 3. 시작점을 방문했다고 표시합니다.
    visited[start] = True

    # 4. 큐가 빌 때까지 반복합니다.
    while queue:
        # 5. 큐에서 현재 숫자와 연산 횟수를 꺼냅니다.
        current_num, count = queue.popleft()

        # 6. 만약 현재 숫자가 목표 숫자와 같다면, 탐색 성공!
        if current_num == end:
            return count # 현재까지의 연산 횟수를 반환하고 종료

        # 7. 다음 상태들을 탐색합니다 (+1, -1, *2, -10 연산).
        # next_num: 연산을 적용한 다음 숫자
        for next_num in [current_num + 1, current_num - 1, current_num * 2, current_num - 10]:
            
            # 8. 다음 숫자가 유효한 범위에 있고, 아직 방문한 적이 없다면
            if 1 <= next_num <= 1000000 and not visited[next_num]:
                
                # 9. 방문했다고 표시하고,
                visited[next_num] = True
                # 10. (다음 숫자, 다음 연산 횟수)를 큐에 추가합니다.
                queue.append((next_num, count + 1))
    
    return -1

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    result = bfs(N, M)
    
    print(f"#{tc} {result}")