# [BFS] 시차의 폭풍은 정말 최고야!

# 선 위에서 진행되는 장기의 말 중 하나인 마(馬)는 위의 그림과 같이 움직입니다.
# 하지만 우연히 시공과 차원의 폭풍에 휘말린 마는 체스판으로 가고 말았습니다.
# 칸으로 진행되는 체스에서 마는 칸(馬)으로 이동을 하게 됩니다.

# | | | | | |
# | | | | | |
# | | | | | |
# | | | | | |
# | | | | | |  => 이런 체스판이라 생각하면 된다. (체스의 "나이트"처럼 8방향으로 움직일수있음)

# 체스판에서의 마와 목적지의 칸이 주어졌을 때, 마는 몇 번 만에 목적지에 갈 수 있는지를 알아내는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에는 정사각형 체스판의 한변의 길이인 정수 l을 입력합니다.
# (4 ≤ l ≤ 200)
# 둘째 줄에는 마가 현재 있는 칸(X_{s}, Y_{s})을 공백을 두고 입력합니다.
# (0 ≤ X_{s}, Y_{s} ≤ l-1)
# 셋째 줄에는 마의 목적지 칸(X_{g}X , Y_{g}공백을 두고 입력합니다.
# (0 ≤ X_{g}, Y_{g} ≤ l-1)
# [출력]
# 마가 몇 번 만에 이동할 수 있는지 출력합니다.

# [입력 예시]
# 5
# 0 0
# 0 4
# [출력 예시]
# 2

from collections import deque

def horse_bfs(graph,start,target):

    queue = deque()
    queue.append((start[0],start[1]))
    temp = deque()
    graph[start[0]][start[1]] = 1
    graph[target[0]][target[1]] = 2

    dx = [-2,-2,-1,1,2,2,-1,1]
    dy = [-1,1,2,2,1,-1,-2,-2]

    count = 0

    while True:

        count += 1

        while queue:

            (x,y) = queue.popleft()

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx < n and 0<= ny < n:
                    if graph[nx][ny] == 0:
                        temp.append([nx,ny])
                        graph[nx][ny] = 1
                    elif graph[nx][ny] == 2:
                        return count  

        if len(temp) != 0:
                queue = temp.copy()
                temp.clear()         
                    

if __name__ == '__main__':

    n = int(input())
    graph = [ [0]*n for _ in range(n)]
    start = list(map(int,input().split()))
    target =  list(map(int,input().split()))

    print(horse_bfs(graph,start,target))


# # 아이디어
# - 결국, 우리에게 익숙한 배열형태로 위에서 움직이겠다는 거고, 장기에서 "말", 체스에서 "나이트"는 8 방향으로 움직일 수 있다.
# - 순서대로, (상좌,상우,우상,우하,하좌,하우,좌하,좌상)
# - BFS로, 현재 스텝에서, 이동할 수 있는 좌표를 이동하면서, 큐에 좌표값을 넣는다.
# - 이때, 이동했을때, 0(아직 방문안함)이면, 좌표값을 큐에넣고, 1(방문함)이면, 무시하고, 2(목적지)이면, 스텝카운터를 반환하도록 한다.

# # 결과
# - 100

# # 질문거리
# - "생체실험"문제도 그렇고, BFS문제인데, "몇 번째만에" 라 키워드가 있으면, 큐를 한번씩 pop하는게 아니라, 한 스텝에 현재 들어가 있는 큐를 다 pop해보고, 한 스텝 넘어가는 방식이 맞는건지 ?

