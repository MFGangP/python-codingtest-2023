class Graph():
    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def makeGraph():
    ## 전역변수 선언 부분
    G1 = None
    stack = []  # 네비게이션 - 내가 가야할 곳 적는곳
    visitedAry = [] # 방문한 기록
    # A = 0, B = 1, C = 2, D = 3
    G1 = Graph(4) # 버텍스 4개 짜리 그래프
    G1.graph[0][2] = 1;G1.graph[0][3] = 1 
    G1.graph[1][2] = 1
    G1.graph[2][0] = 1;G1.graph[2][1] = 1;G1.graph[2][3] = 1
    G1.graph[3][0] = 1;G1.graph[3][2] = 1

    print('## G1 무방향 그래프 ##')
    for row in range(4):    # 4개짜리 배열을 보여줄거야
        for col in range(4):# 4x4짜리로 만들거야
            print(G1.graph[row][col],end=' ')
        print() # 한 줄 띄워

    current = 0 # 현재 내가 있는 곳 = 0
    stack.append(current) # 네비게이션 현재 위치 = 0
    visitedAry.append(current) # 방문 기록 = 0

    # 1인 곳만 가는거지 0인 곳을 가는게 아니라서 순서대로 가는게 아니라는걸 알아야함
    # 1,2,3,4,5 로 가는게 아니고 1,7,3,8,4 이렇게 막 갈 수 있다는 소리
    # 자동차 타고 놀러가는데 네비찍고 인스타 맛집을 찾으러 돌아다니는 느낌        
    # 버텍스(원소) 값이 1인 것 = 인스타 맛집
    # current = 내 차 현재 위치
    # vertex = 맛집 검색
    # stack = 네비게이션 길 안내
    # visitedAry = 네비게이션 방문 기록
    
    while(len(stack) != 0): # 스택이 비어있지 않으면 무한 루프
        next = None # 다음에 가야할 곳 초기화
        for vertex in range(4): # 버텍스(원소)개수만큼 반복 할 거야
            if G1.graph[current][vertex] == 1: # 만약 current][vertex]이 가야하는 곳일 때
                                               # 먼저 나타나는 놈부터 갈게~
                if vertex in visitedAry: # 방문기록이 있다면
                    pass                 # 응~~ 안가~~
                else:                    # 방문기록이 없네?
                    next = vertex        # 다음에 가야할 곳은 [current][vertex]니까
                    break                # 버텍스 쪽에 놀러가서 다른데를 가볼까
   
        if next != None:    # 가야할 곳이 있다면
            current = next  # 다음에 가야 할 곳 위치를 현재 내 위치으로 옮기고
            stack.append(current)   # 네비게이션에 위치 추가
            visitedAry.append(current) # 방문 기록에도 위치 추가
        else :
            current = stack.pop()   # 가야 할 곳이 없네? 네비게이션 안내 종료 ㅅㄱㅂ
                                    # 응 다른데 갈거야~ while 문 처음으로 돌아가
    print('방문 순서 -->', end=' ')
    for i in visitedAry:
        print(chr(ord('A')+i),end='')

if __name__ == '__main__':
    makeGraph()