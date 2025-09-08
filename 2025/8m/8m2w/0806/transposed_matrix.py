# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3 행렬

for i in range(3):
    for j in range(3): # for j in range(i):인 경우
        # 값이 변경되는 기준이 들어갈 자리
        if i < j: # if문 필요 없음
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]