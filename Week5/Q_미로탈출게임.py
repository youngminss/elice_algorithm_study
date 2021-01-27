# [(BFS)/DFS] 미로 탈출 게임

# 엘리스는 친구들과 함께 미로 탈출 게임을 하기로 했습니다. 게임은 미로를 탈출하는데 가장 적은 칸을 지나간 사람이 이기는 방식으로 진행됩니다.
# 미로는 N * N 크기의 배열로 구성되어 있습니다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타냅니다.
# 이러한 미로가 주어졌을 때, 출발지 (1, 1)에서 도착지 (N, N)의 위치로 이동할 때 지나야 하는 최소 칸의 수를 구하는 프로그램을 작성하세요.
# 칸을 셀 때는 시작 위치와 도착 위치도 포함됩니다.
# 예를 들어 5 * 5 미로가 다음과 같이 주어졌을 경우
# 10111
# 10101
# 10101
# 10101
# 11111
# 다음이 최소의 칸을 지나는 경로이므로
# 1 0 1 1 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 1 1 1 1
# 9가 출력됩니다.

# [입력]
# 첫째 줄에 정수 N을 입력합니다.
# (2 ≤ N ≤ 50)
# 둘째 줄부터 N+1개의 줄에는 0과 1로 구성된 N개의 미로가 주어지며, 각각의 수들은 붙어있어야 합니다.
# 항상 도착 위치로 이동할 수 있는 경우만 입력으로 주어집니다.
# [출력]
# 도착할 때까지 지나가야 하는 최소 칸의 수를 출력합니다.

# [입력 예시]
# 5
# 10111
# 10101
# 10101
# 10101
# 11111
# [출력 예시]
# 9

from collections import deque

def maze_bfs(graph,n):

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1

    queue = deque()
    queue.append((0,0))

    while queue:
        (x,y) = queue.popleft()
        if x == n-1 and y == n-1:
            return visited[n-1][n-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1


if __name__ == '__main__':
    n = int(input())
    maze = []
    for i in range(n):
        temp = []
        input_line = input()
        for j in range(len(input_line)):
            temp.append(int(input_line[j]))
        maze.append(temp)
    
    print(maze_bfs(maze,n))


# # 아이디어
# - n * n 미로를 입력받고, 그것과 동일한 크기의 n * n 방문배열을 만든다.
# - 미로배열을 상하좌우 BFS로 한칸씩 보면서, 이동해도되는조건(1이고, 방문배열에서 아직 방문안했으면) 이동
# - 방문배열에 들어가는 값은, 그 (i,j)까지 가는데, 걸리는 칸 수

# # 결과
# 1004

