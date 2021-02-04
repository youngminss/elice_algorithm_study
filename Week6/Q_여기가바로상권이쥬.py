# [BFS] 여기가 바로 상권이쥬

# 유명한 음식 사업가인 백벨원의 음식점들은 음식의 맛 뿐만 아니라 좋은 상권에 자리를 잡는 것으로 유명합니다.
# TV에 출연한 백벨원은 자신의 노하우를 사람들에게 알려주었습니다.
# 백벨원의 노하우는 다음과 같습니다.

# 0 1 1 1 0 0 1 1
# 0 1 0 1 0 0 1 1
# 0 1 1 1 0 0 1 1
# 0 0 0 0 0 0 0 0
# 0 0 1 1 1 1 1 0 
# 0 0 1 1 1 1 1 0
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 1 1 1 1

# 위의 그림처럼 N * N 크기의 정사각형 지도에서 주택가를 1, 주택가가 아닌 곳을 0으로 표시를 합니다.
# 어떤 집의 좌우, 혹은 아래위로 다른 집이 있는 경우 그 집들을 하나로 묶습니다. 이 묶음을 상권이라고 이름을 붙입니다.
# 상권을 지도상에 아래와 같이 구분합니다.
# 위의 그림에서는 상권은 총 4개이며, 그 상권에 속하는 각각의 집의 수는 8, 6, 10, 4 입니다.
# 백벨원의 노하우를 적용하여 지도가 입력됐을 때, 상권의 수를 출력하고 각 상권에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하세요.

# [입력]
# 첫째줄에는 정사각형 지도의 크기 N을 입력합니다.
# (5≤N≤25)
# 그 다음 N줄에는 지도의 정보(0 또는 1)를 입력합니다.
# [출력]
# 첫째줄에 총 상권의 수를 출력합니다.
# 각 상권내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력합니다.

# [입력 예시]
# 8
# 01110011
# 01010011
# 01110011
# 00000000
# 00111110
# 00111110
# 00000000
# 00001111
# [출력 예시]
# 4
# 4
# 6
# 8
# 10

from collections import deque

def maps_bfs(arr,graph,result,i,j):

    queue = deque()
    queue.append((i,j))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    graph[i][j] = 1

    count = 0
    while queue:
        (x,y) = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx,ny))
                count += 1
                graph[nx][ny] = count
    if count == 0:
        result.append(1)
    else:
        result.append(count)

if __name__ == '__main__':
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        temp = input()
        for j in range(n):
            if int(temp[j]) == 1:
                arr[i][j] = 1
            
    graph = [([0]*n) for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and graph[i][j] == 0:
                maps_bfs(arr,graph,result,i,j)

    result.sort()
    print(len(result))
    for r in result:
        print(r)


# # 아이디어
# - 결국, 한 개라도 1 로 둘러쌓여있는경우, 상관 1개로 생각한다.
# - (0,0) 위치부터, 주택가를 의미하는 1 값이 존재할 때부터, 그 곳에 연결되어있는, 주택가(1)을 BFS로 구한다.
# - BFS의 각 원소는, 이전 칸 까지의, 주택가 수의 누적
# - 그렇게 BFS로 돌다가, 상하좌우로, 이동할 곳이 없으면, 한 상권 BFS 순회 끝 !
# - 이런 방식으로, (0,0) ~ (n,n) 까지의, 조건에 맞으면, BFS를 순회해서, 결과적인, 각 상권의 크기 배열을 구한다.

# # 결과
# 100
