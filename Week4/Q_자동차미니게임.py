# [(DFS)/BFS ] 자동차 미니 게임

# N* M 사이즈의 미니 게임판이 있습니다. 미니 게임은 자동차를 게임판에서 주행하는 게임입니다.
# 미니게임에서 자동차가 주행하는 방법은 다음과 같습니다.
# 게임판은 칸마다 0에서 9까지의 숫자가 적혀있습니다.
# 자동차는 한번에 각 칸에 적힌 숫자만큼 이동하며 →, ↓, ←, ↑방향 중 하나를 골라 움직일 수 있습니다.
# 자동차가 다음으로 움직일 칸이 게임판 밖으로 나가거나 ‘0’이 적힌 칸인 경우 게임은 종료됩니다.
# 왼쪽 위(0,0)는 자동차의 출발지이며, 칸에 적힌 숫자가 0이 될 수 없습니다.
# 미니 게임판을 줬을 때 자동차가 출발 전, 정차할 칸이 가장 많은 경로를 정합니다. 게임이 종료될 때까지 정차한 칸의 개수를 출력하는 프로그램을 작성하세요.
# (※출발 칸도 정차한 칸의 개수에 포함합니다.)

# [입력]
# 첫 번째 줄에 게임판의 세로의 길이인 자연수 N, 가로의 길이인 자연수 M을 입력합니다.
# (1≤N, M≤50)
# 두 번째 줄부터 게임판의 모양대로 숫자를 입력합니다.
# [출력]
# 첫 번째 줄에 자동차가 정차한 칸의 개수 최댓값을 출력합니다.
# (※ 자동차가 게임판에서 움직일 수 있는 칸이 무한대인 경우 ‘-1’을 출력합니다.)

# [입력 예시]
# 3 5
# 21012
# 51213
# 61133
# [출력 예시]
# 2

import sys
count = 0

def ski_dfs(arr,dfs_arr,stack,n,m):
    
    global count
    count += 1
    if count >= 1000:
        print(-1)
        sys.exit()

    (i,j) = stack[-1]
    move_num = arr[i][j]

    if 0<=(i - move_num)<n and arr[i-move_num][j] != 0 and dfs_arr[i-move_num][j] == 0:
        dfs_arr[i-move_num][j] = dfs_arr[i][j] + 1
        stack.append((i-move_num,j))
        ski_dfs(arr,dfs_arr,stack,n,m)

    if 0<=(j+move_num)<m and arr[i][j+move_num] != 0 and dfs_arr[i][j+move_num] == 0:
        dfs_arr[i][j+move_num] = dfs_arr[i][j] + 1
        stack.append((i,j+move_num))
        ski_dfs(arr,dfs_arr,stack,n,m)

    if 0<=(i+move_num)<n and arr[i+move_num][j] != 0 and dfs_arr[i+move_num][j] == 0:
        dfs_arr[i+move_num][j] = dfs_arr[i][j] + 1
        stack.append((i+move_num,j))
        ski_dfs(arr,dfs_arr,stack,n,m)

    if 0<=(j-move_num)<m and arr[i][j-move_num] != 0 and dfs_arr[i][j-move_num] == 0:
        dfs_arr[i][j-move_num] = dfs_arr[i][j] + 1
        stack.append((i,j-move_num))
        ski_dfs(arr,dfs_arr,stack,n,m)
    
    stack.pop()
    if len(stack) == 0:
        return None
    

if __name__ == '__main__':
    n, m = map(int,input().split())
    temp = [input() for _ in range(n)]
    dfs_arr = [[0]*m for _ in range(n)]
    arr = []
    for data in temp:
        num_list = []
        for i in range(len(data)):
            num_list.append(ord(data[i])-ord('0'))
        if len(num_list) != 0:
            arr.append(num_list)
    dfs_arr[0][0] = 1
    stack = [(0,0)]
    
    ski_dfs(arr,dfs_arr,stack,n,m)
    
    result = 0
    for data in dfs_arr:
        if result < max(data):
            result = max(data)
    print(result)


# # 아이디어
# BFS로 풀었다. n * m 크기의 추차배열을 받으면, 그것과 같은 모든 원소가 0으로 초기화된 배열을 하나 더 만들었다.
# 재귀적으로, 반복할 건데, 처음 시작위치(0,0)에서부터 시작해서, 
# 1. 매번, 주차배열의 원소값 만큼 더한, "상하좌우" 인덱스를 봐서 가도되는 곳이고
# 2. 1번이 만족했을 때, 주차배열에서도, 원소값만큼 이동한 곳에, '0' 이 아니어야하고
# 3. 1,2 번이 만족했을때, 복사한 배열(방문배열)에서 0 인 곳 (아직 방문하지 않은 곳)이면
# 방문배열에 들어가는 값은, (현재 시점에서의 정차 최대값 + 1) 이다.
# 이러한 작업이, 끝나는 시점은
# (1) 주차배열에 일단, 0 이 하나라도 있는 경우(반드시 재귀는 끝남)
# = 스택이 비워지면 끝
# (2) 무한적으로 움직이는 경우
# = 요게문젠데,,일단 나는 재귀가 1000번 정도 이상 돌면, 뭔가 무한정으로 이동할 수 있는 상황이라 생각하고, -1 출력후, 시스템을 종료하게 했다. (야매느낌..)   
  

# # 결과
# 100

# # 질문거리
# 일단, 푼거는 DFS 풀었다. 그러나..풀이가 너~무 깔끔하지 못하다. 동일한 작업도, 원래같으면 메소드화 해야되는데, 오래 붙잡고 있어서, 멘탈이 나가서, 푸는데만  신경썼다.
# 이 문제를 DFS로 풀어나갈경우, 내가 생각해낸 로직이 정답이었던 방향이었는지 ?
# 무한정, 이동할 경우의 예시를 좀 알았으면 좋겠다.
# 그리고, 그럴 경우를, 어떻게 제어 했어야 했는지 알고 싶다.
# (다른분은 BFS로 풀었는데, 처음부터, 발상을 그쪽으로 해볼 걸 그랬다.)
