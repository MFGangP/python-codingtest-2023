# 단순 연결 리스트 구현
# 노드 생성하는 클래스
class Node:
    def __init__(self):
        self.data = None
        self.link = None

# 전역 변수
memory = [] # list()
head, current, pre = None, None, None   # 변수 초기화
dataArray = ['다현', '정현', '쯔위', '사나', '지효']    # 리스트 선언

def printNode(start):   # 노드 보여주는 함수
    current = start
    if current == None:
        return
    print(current.data, end=' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data,)
        else:
            print(current.data, end=' -> ')

# 노드 추가

def insertNode(findData, insertData):
    global memory, pre, current, head 
    # 첫노드 앞에다 데이터를 넣겠다면
    if head.data == findData:   # 맨 앞의 데이터가 찾는 데이터라면
        node = Node() # 새로운 노드를 만들고
        node.data = insertData # 입력 받은 인서트 데이터를 노드 데이터에 삽입
        node.link = head   # 노드 링크를 헤드에 연결
        head = node # 맨 앞의 노드를 삽입한 노드로 변경
        # 결과적으로 기존의 헤드 데이터는 인서트 데이터로 변경된거고, 
        # 새로운 노드 데이터가 헤드 데이터가 된 것
        return

    current = head # current를 제일 앞으로
    # current 노드를 지금의 head 데이터로 덮어 쓰고
    while current.link != None: # current.link가 마지막이 아닐동안 
                                # 계속 돌면서 중간노드 추가
        pre = current # pre 노드를 current랑 똑같이 만들어주고
                      # 현재 current는 head 노드
        current = current.link # current노드는 하나 더 뒤로 가기
                               # 결과적으로 pre, current 

        if current.data == findData: # 만약에 current 데이터가 찾는 데이터면
            node = Node() # 새로운 노드를 만들어서
            node.data = insertData # 새 노드 데이터를 삽입 하려고 하는 데이터로 만들고
            node.link = current # 새 노드 링크는 current로 연결
            pre.link = node # pre와 current 중간에 새로 생성한 node가 들어감
            return
            # pre , node , current 순

    # current.link == None 까지 온 것
    node = Node()
    node.data = insertData
    current.link = node
    return

# 노드 삭제

def deleteNode(deletedData):
    global memory, pre, current, head

    if head.data == deletedData:# 첫번째 노드가 삭제해야하는 노드면
        current = head  # current노드가 head를 보게 만듦
        head = head.link # head 노드를 두번째 노드로 변경
        del(current)    # current 삭제
        return          # 결과적으로 head가 첫번째 노드가 됌

    # 삭제하려고 했던 노드가 첫번째 노드가 아니였다면
    current = head  # current도 첫번째 노드
    while current.link != None: # 첫번째 이외 노드 삭제
        pre = current   # 모두 첫번째 노드 가리킴
        current = current.link # 두번째 노드 가리킴
        if current.data == deletedData: # current 데이터가 삭제해야하는 데이터면
            pre.link = current.link # current가 가리키는 노드를 pre가 가리킴
            del(current)
            return

# 노드 검색

def findNode(findData):
    global memory, pre, current, head

    current = head  # 첫 번째 노드를 가리킴
    if current.data == findData: # 지금 보는 노드의 데이터가 찾는 데이터면
        return(current) # 현재 노드 반환
    while current.link != None: # None이 나올 때 까지 
        current = current.link # 현재 보는 노드를 다음 노드로 변경
        if current.data == findData: # 다음 노드가 찾는 데이터라면
            return current # 데이터 반환
    return Node() # 다 돌았는데 안나오면 빈노드 반환

if __name__ == '__main__':
    node = Node() # 객체, 클래스 생성자
    # 빈 노드를 node라는 이름으로 만든다.
    node.data = dataArray[0] # 빈 노드에 dataArray[0]번인 다현 삽입
    head = node  # head를 새로 만든 노드 데이터랑 같게 만들기 
    memory.append(node) # 메모리에 새로만든 노드 더하기
    # head == node

    for data in dataArray[1:]: # 두번째 노드 이후 4번 반복
        pre = node  # pre가 '다현'을 가리킴
        node = Node()   # node를 새로운 노드로 바꿈
        node.data = data    # data 내부 값은 정연, 쯔위, 사나, 지효 순
        # 새로 만든 노드 데이터를 다음 값인 쯔위로 삽입
        pre.link = node # pre 노드가 가르킬 다음 노드를 node로 지정
        memory.append(node) # 메모리에 node 추가
    # head 맨 앞, pre는 내가 새로 만든 값 바로 앞의 값
    printNode(head) # 전체 출력

    print('노드 추가 --------------')

    insertNode('다현', '화사')  # 맨 앞에 화사 노드 추가
    printNode(head)

    insertNode('사나', '솔라')  # 사나 앞에 솔라 노드 추가
    printNode(head)

    insertNode('재남', '문별')  # 재남이 없기 때문에 맨 마지막에 문별 추가
    printNode(head)

    print('노드 삭제 --------------')

    deleteNode('화사')
    printNode(head)

    deleteNode('지효')
    printNode(head)
    
    deleteNode('재남')  # 삭제할 데이터가 없음.
    printNode(head)     # 그전이랑 똑같이 나옴

    print('노드 검색 --------------')

    result = findNode('정현') 
    if result.data != None:
        print('검색한 데이터가 존재합니다.')
    else:
        print('검색한 데이터가 존재하지 않습니다.')

    result = findNode('재남') 
    if result.data != None:
        print('데이터가 존재합니다.')
    else:
        print('검색한 데이터가 존재하지 않습니다.')
