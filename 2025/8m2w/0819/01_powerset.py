lst = [1,2,3,4,5]

N = 5

# 부분 집합의 합이 S 이하인 부분 집합만 구하세요
S = 5

# 부분 집합을 만드는 재귀 함수
# make_set(0) : 0번 원소를 부분 집합에 넣을지 말지
# make_set(1) : 1번 원소를 부분 집합에 넣을지 말지


# make_set(N-1) : N-1번 원소를 부분 집합에 넣을지 말지
# make_set(N) : N 번 원소는 없음 => 재귀 호출 중단.

# idx : 내가 지금 idx번 원소를 부분 집합에 넣을지 말지 선택
# selected 리스트 : 내가 지금까지 고른 부분 집합에 포함할 원소들의 상태를 나타내는 변수
# visited랑 똑같은 역할
# selected[x] == 1 (True) : x번 원소를 부분집합에 넣기로 했다.
# selected[y] == 0 (False) : y번 원소를 부분집합에 넣지 않기로 했다.

# 현재까지의 합을 알고 있으면 언제 종료해야하는지 쉽게 알 수 있다.
# s : idx번 원소까지 부분 집합에 넣을지 말지 고민을 하고 있는데, 
#     이때까지 완성한 부분 집합의 합
def make_set(idx, selected, s):
    # 0. 가지치기
    # 지금까지 구한 부분 집합의 합 s가
    # 문제에서 원하는 합 S보다 크면 더 진행 xxx (답이 될 확률이 없음)
    if s > S:
        return

    # 1. 종료 조건 설정
    if idx == N:
        # selected 배열을 보고 내가 어떤 원소를 선택했었는지 확인
        subset = []
        for i in range(N):
            # 내가 i번 원소를 부분집합에 포함하기로 했었다면
            if selected[i]:
                subset.append(lst[i])
        print(subset)

        # 백트래킹을 안배웠으면 여기서 값 판단을 하고 있었을것
        # if sum(subset) <= S:
        #   print(subset)
        return

    # 2. 재귀 호출 - 이 단계에서 다음 단계로 어떻게 진행할거냐
    # idx번 원소를 부분 집합에 넣고 idx+1번 원소를 판단하기
    selected[idx] = 1
    make_set(idx+1, selected, s+lst[idx])
    # idx번 원소를 부분 집합에 넣지않고 idx+1번 원소를 판단하기
    selected[idx] = 0
    make_set(idx+1, selected, s)

# 처음부터 시작하는 재귀함수 호출이 필요하다.
# 0부터 부분집합에 넣을지 말지 고민하기 시작
make_set(0, [0] * N, 0)

def make_set2(idx, selected, s):
    # 0. 가지치기
    # 지금까지 구한 부분 집합의 합 s가
    # 문제에서 원하는 합 S보다 크면 더 진행 xxx (답이 될 확률이 없음)
    if s > C:
        return

    # 1. 종료 조건 설정
    if idx == N:
        # selected 배열을 보고 내가 어떤 원소를 선택했었는지 확인
        subset = []
        for i in range(N):
            # 내가 i번 원소를 부분집합에 포함하기로 했었다면
            if selected[i]:
                subset.append(lst[i])
        print(subset)

        # 백트래킹을 안배웠으면 여기서 값 판단을 하고 있었을것
        # if sum(subset) <= S:
        #   print(subset)
        return

    # 2. 재귀 호출 - 이 단계에서 다음 단계로 어떻게 진행할거냐
    # idx번 원소를 부분 집합에 넣고 idx+1번 원소를 판단하기
    selected[idx] = 1
    make_set2(idx+1, selected, s+lst[idx])
    # idx번 원소를 부분 집합에 넣지않고 idx+1번 원소를 판단하기
    selected[idx] = 0
    make_set2(idx+1, selected, s)

# 원소의 개수가 c개 이하인 부분 집합만 출력
C = 2

make_set(0, [0] * N, 0)