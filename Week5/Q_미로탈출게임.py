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