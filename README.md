# python-codingtest-2023
파이썬 코딩 테스트 리포지토리

# 1일차
1. 코딩테스트 소개
    - 백준
    - 프로그래머스
    - SW Expert Academy
2. 코딩테스트 학습
    - 자료구조 - 배열/리스트
    - 구간 합

카카오 인턴쉽 코딩 테스트를 프로그래머스에서 하는걸 봐서 익숙한 플랫폼들이였다.
자료구조 들어가니까 한번에 바로 이해 되지는 않게 되었으나, 주석달면서 천천히 읽으면 이해되는 상태

# 2일차
파이썬 파일 명에는 '_'만 사용할 것

1. 코딩테스트 학습
    - 구간합 2
    - 자료구조 다시
        - 연결리스트
        - 스택
        - 큐
    - 외부 모듈 스택 확인

# 3일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 큐
        - [x] 이진트리
            - 삭제는 연결 리스트 삭제와 유사
            - 자식 노드가 두개 이상일 때는 어려울 수 있음
        - [x] 그래프

# 4일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 그래프(DFS)
        - [x] 재귀 호출
        - [x] 정렬(선택, 삽입, 버블, 퀵) 이론

# 5일차
1. 코딩테스트 학습
    - 자료구조 / 알고리즘
        - [x]정렬(선택, 삽입, 버블, 퀵) 실습
        - [x]검색
        - [x]동적 계획법 [다이나믹 프로그래밍] / 피보나치 실행시간 비교
        
# 6일차
1. 코딩테스트 학습
    - 자료구조
        - [x]deque (덱)
    - 코딩테스트 알고리즘       
        - [x] 큐 포인터
        - [x] 슬라이딩 윈도우
        - [x] 정렬
    - README 사용법(체크박스)
```python
# 이건 기수정렬이 아니다. 계수 정렬
N = int(input()) # N 개 만큼 숫자를 받을거다
count = [0] * 10001 # 10000까지 할거라서 1 여유분

for i in range(N):  # N개 만큼 반복
    count[int(input())] += 1 # 입력한 숫자를 count[입력값]에 넣고 값 1 더하기

for i in range(10001): # 10001개 만큼 반복 
    if count[i] != 0: # 값이 0이 아니면(0이면 굳이 표시할 필요가 없음)
        for _ in range(count[i]): # 0해당하는 숫자에 해당하는 횟수 만큼
            print(i)    # 인덱스 값 출력
```

# 7일차
1. 코딩테스트 학습
    - 자료구조
        - [x] 그래프
        - [x] PriorityQueue (우선순위 큐)
        - [x] heapq (힙큐)
    - 알고리즘
        - [x] 탐색 - DFS(스택)/BFS(큐)/이진탐색
        - [x] 그리디
        - [x] 정수론

# 8일차
1. 코딩테스트 학습
    - 자료구조
        - 심화
            - 그래프
                - 에지 리스트
                - 인접 행렬
                - 인접 리스트
                    - 가중치가 변하지 않기 때문에 튜플로 넣어도 괜찮다. 
    - 알고리즘
        - [ ] 정수론
        - [ ] 그래프 활용
