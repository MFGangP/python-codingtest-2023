lst = [1,2,3]
N = 3

# 자리의 주인을 지목하는 방식
# 완성된 순열의 길이도 3
# 0번 인덱스에 누가 올래? : make_perm(0)
# 1번 인덱스에 누가 올래? : make_perm(1)
# ...

# N-1번 인덱스에 누가 올래? : make_perm(N-1)
# N번 인덱스에 누가 올래? : make_perm(N) => XXXX 재귀 중단. 
# idx : 완성된 순열의 idx번 자리에 사용할 원소 선택
# visited : 순열을 만들 떄 이전에 사용한 원소는 사용 불가, 체크용
# visited[x] == 1 : x번 원소는 이전에 순열 만들 때 사용함.
# visited[y] == 0 : y번 원소는 이전에 사용한 적이 없음 
# => idx 자리에 y번 원소가 올 수 있다.

# result : idx 단계까지 완성된 순열
def make_perm(idx, visited, result):
    # 0.

    # 1. 종료 조건 세우기
    if idx == N:
        # 지금까지 만든 순열 출력
        print(result)
        return
    # 2. 재귀 호출
    # idx번 자리에 누가 올거냐? 선택
    # N개 중에 하나 선택할껀데 => 이전에 선택한적 있는 원소는 선택하면 안된다.
    # 모든 원소를 확인해보기 위해 N번 돈다
    for i in range(N):
        # i번 원소를 이전에 순열 만들 때 쓴적 없다 => idx번 위치에 올 수 있다.
        # if not visited[i]:
        if visited[i] == 0:
            # 순열의 idx번 자리에 i번 원소를 놓고 idx+1번 자리에 누가 올지 고민
            visited[i] = 1
            # 순열 만들기, lst의 i번 원소를 사용
            result.append(lst[i])
            # pop() 쓰기 싫다 하면
            # make_perm(idx+1, visited, result + [lst[i]])
            make_perm(idx+1, visited, result)
            # i번 원소를 idx 자리에 놓은 경우의 수는 모두 고려 완료
            # i+1번 원소를 놓기 시작, i번 원소는 사용하지 않았다로 고쳐야한다.
            visited[i] = 0
            # 
            result.pop()
            
# 0번 자리에 누가 올지, 아직 아무도 고른적 없고, 순열은 미완성
make_perm(0, [0] * N, [])