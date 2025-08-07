arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[20,21,22,23,24]]
[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11,12,13,14,15],
[16,17,18,19,20],
[20,21,22,23,24]
N=5

result = 0

for i in range(N):
    for j in range(N):
        result = arr[2][2]
        for di, dj in [[1,1], [1,-1], [-1,-1], [-1,1]]:
            for c in range(1, 3):
                ni, nj = i+di*c, j+dj*c
                if 0<=di<N and 0<=dj<N :
                    result += arr[di][dj]
print(result)