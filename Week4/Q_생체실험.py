# [BFS] 생체 실험

# 어느 연구소에서 신종 바이러스의 전염에 대한 생체 실험을 진행한다고 합니다.
# 실험은 MxN 칸의 격자 모양 상자에서 이루어집니다. 상자의 각 칸에는 바이러스에 전염된 생쥐 혹은 정상 생쥐가 있거나 비어있습니다.
# 실험이 시작되고 하루가 지나면 바이러스에 전염된 생쥐는 인접한 곳에 있는 정상 생쥐들에게 바이러스를 전염시킨다고 합니다.
# 바이러스는 대각선 방향으로는 퍼지지 못하며 인접한 상하좌우 방향으로만 전염됩니다.
# 실험 상자의 크기와 실험에 사용된 생쥐들의 정보가 주어졌을 때, 모든 생쥐가 전염되려면
# 얼마나 걸리는지 최소 일수를 구하는 프로그램을 작성하세요.

# [입력]
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M, N을 입력합니다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타냅니다.
# (2 ≤ M, N ≤ 40)
# 둘째 줄부터 N개의 줄에는 상자에 담긴 생쥐의 정보를 입력합니다. 하나의 줄에는 상자 가로줄에 들어 있는 생쥐의 상태가 M개의 정수로 주어집니다.
# 정수 1은 감염된 생쥐, 정수 0은 정상 생쥐, 정수 -1은 비어있는 칸을 나타냅니다.
# [출력]
# 모든 생쥐가 전염될 때까지의 최소 날짜를 출력합니다.
# 만약, 실험이 시작될 때 모든 생쥐가 전염된 상태이면 0을 출력해야 하고, 생쥐가 모두 전염되지는 못하는 상황이면 -1을 출력해야 합니다.

# [입력 예시]
# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# [출력 예시]
# 8

from collections import deque

def solution():

    n, m = map(int,(input().split()))
    lst = [list(map(int,input().split())) for _ in range(m)]

    def bfs_virus(graph,m,n):
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        queue = deque()
        temp = deque()
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    queue.append((i,j))
    
        if len(queue) == m * n:
            return 0
        
        result = 0
        while True:
            
            while queue:
                (x,y) = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0<= ny <n:
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = 1
                            temp.append((nx,ny))
                  
            if temp:
                result += 1
                queue = temp.copy()
                temp.clear()
            else:
                break

        for g in graph:
            if 0 in g:
                return -1
        
        return result

    result = bfs_virus(lst,m,n)
    print(result)
        

if __name__ == '__main__':
    solution()


# # 아이디어
# - 일단 시작 시, 고려해야될 상황은 3가지
# - 1. 한 부분에서만 감염 쥐가 있는 경우
# - 2. 부분분분 감염 쥐가 있는 경우
# - 3. 시작부터, 모든 쥐가 감염된 경우

# - 매 차례, 큐에 있는 모든, 지점으로부터, 상하좌우 이동을 하면서, 정상인 쥐의 위치를 매번 다시 push해야한다.
# - 큐 하나를 두고, 이 과정을 하려고하면, 매 차례, 끝까지 텅텅 비워버리는 큐 때문에, 한번만 반복문 돌고 끝난다.(날짜가 항상 1이 나옴..) 그래서, 매 차례 돌면서, 정상 쥐의 위치를 담은 임시 큐를 사용했다.

# # 결과
# 100

# # 질문
# - 초반에, 2차원 리스트에서  큐에, 감염된 쥐(1)의 좌표를 찾는데, 일일히 반복문을 썻는데, O(n^2) 이 항상 되버리는데, 좀더 효율적인 방법이 있는지 ?
