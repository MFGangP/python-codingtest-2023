import heapq

# 힙으로 사용할 배열
heap = []

lst = [6, 5, 4, 1, 3, 2, 9, 8, 10, 7]

for i in range(10):
    # 여기에 -lst[i] 로 쓰면 - 붙어서 큰 값이 먼저오게 된다.
    # 값 하나 더 넣어서 튜플로 값을 낼 수도 있다.
    heapq.heappush(heap, lst[i])

for i in range(10):
    print(heapq.heappop(heap), end=" ")

print()