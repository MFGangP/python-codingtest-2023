class Graph():
    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None
nameAry = ['문별', '솔라', '휘인', '쯔위', '선미', '화사']
문별, 솔라, 휘인, 쯔위, 선미, 화사 = 0, 1, 2, 3, 4, 5
# 그래프 그리기 함수

def printGraph(graph):
    print('     ', end=' ')
    for v in range(graph.SIZE):
        print(nameAry[v], end=' ')
    print()

    for row in range(graph.SIZE):
        print(f'{nameAry[row]}', end=' ')
        for col in range(graph.SIZE):
            print(f'   {graph.graph[row][col]}', end=' ')
        print()
    print()

# 메인코드

if __name__ == '__main__':
    gSize = 6
    G1 = Graph(gSize)
    # 한 줄에 두 줄 이상 쓰고싶다 할 때 ;(세미콜론) 쓰면된다.
    G1.graph[문별][솔라] = 1; G1.graph[문별][휘인] = 1
    G1.graph[솔라][문별] = 1; G1.graph[솔라][쯔위] = 1
    G1.graph[휘인][문별] = 1; G1.graph[휘인][쯔위] = 1
    G1.graph[쯔위][솔라] = 1; G1.graph[쯔위][휘인] = 1; G1.graph[쯔위][선미] = 1; G1.graph[쯔위][화사] = 1
    G1.graph[선미][쯔위] = 1; G1.graph[선미][화사] = 1
    G1.graph[화사][쯔위] = 1; G1.graph[화사][선미] = 1

    print('무방향 그래프')
    printGraph(G1)

    # 리스트 가지고 스택 구현
    # 리스트기 때문에 인덱스 0부터 뽑을 수 있으니까 주의
