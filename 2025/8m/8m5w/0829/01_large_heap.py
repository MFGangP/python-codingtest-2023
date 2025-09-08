# 최대 힙으로 사용할 배열
heap = [0] * 11
# 마지막으로 넣은 원소의 위치를 기억
last = 0

# 삽입
def enq(item):
    global last
    # item을 맨 마지막에 넣은 자리 +1 한 자리에 넣고
    # 맨 마지막 위치 : last +1
    last += 1
    heap[last] = item

    # 일단 넣어봤는데 여기가 니 자리가 맞니???
    # 최대 힙 : 부모 > 자식
    # item의 크기와 부모 노드의 크기를 비교해서 교환
    child = last
    # 완전 이진 트리 이므로 부모 = 자식 // 2
    parent = last // 2

    # child에 있는 값과 parent에 있는 값을 비교
    # 부모 원소와 비교하면서 그 자리가 맞는지 확인
    # 부모 노드가 존재하고, 부모 노드보다 자식이 크면
    # 자리를 계속 교환
    # 부모 노드의 인덱스 번호가 0이면 부모 노드가 없는 것.
    # 왜냐 첫 데이터 삽입을 인덱스 1부터 시작했기 때문에
    while parent != 0 and heap[child] > heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        # 부모의 부모가 새로운 부모가 되고    
        child = parent
        parent = child // 2

# 삭제
def deq():
    global last
    # 삭제를 하면 되돌려줘야 하는 값을 알지 못하니 저장 해놔야한다.
    # 루트 노드 삭제 전에 기억
    root = heap[1]
    # 마지막 위치에 있는 원소를 루트 자리로 땡겨온다
    heap[1] = heap[last]
    # 원소 하나 제거했으니까 위치도 하나 줄어들어야한다.
    last -= 1
    
    # 일단 루트 자리에 마지막 원소 땡겨오긴했는데
    # 거기가 니 자리가 맞아???

    # 부모 > 자식
    # 부모는 1번 부터 시작할거고
    # 완전 이진 트리이니까 오른쪽 만 있는 경우는 없다.
    p = 1
    c = p * 2 # 왼쪽 자식

    # 자식이 두명 있으면 그중에 큰 자식과 비교해서
    # 부모와 자리 교환
    while c <= last:
        # c가 last 이하라는 건 왼쪽 자식은 있다는거고 오른쪽 자식도 비교 해봐야한다.
        # 오른쪽 자식이 있다는건 오른쪽 자식도 last보다 작아야한다,
        # c+1 : 오른쪽 자식 번호
        # 이 오른쪽 자식이 존재하는가.
        # 오른쪽 자식이 왼쪽 보다 큰가
        if c + 1 <= last and heap[c] < heap[c+1]:
            # 그렇다면 비교 자식은 오른쪽으로
            c = c + 1
        # 자식 두명 중에 큰 애를 골랐고 걔를 부모랑 비교해서 교환
        # 자식이 부모보다 큰지 확인하고 교환
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c # 자식이 새로운 부모
            c = c * 2 # 새로운 보모 기준 왼쪽 자식
        else:
            # 부모가 자식보다 크면 맞는 자리라서 자리 바꾸기 중단.
            # 자리 바꾸기 중단
            break
    return root

lst = [6, 5, 4, 1, 3, 2, 9, 8, 10, 7]

for i in range(10):
    enq(lst[i])
print(heap)

for i in range(10):
    # 큰 값 부터 나오니까 내림차순 정렬
    print(deq(), end=", ")
    # 최소 힙은 오름차순 정렬