# [BFS- SP] 자원 절약 운동
# 어떤 지역에서 생산한 제품을 다른 지역에 판매하려면 생산지 가격에 다른 지역까지의 운송비가 더해진 가격에 판매되게 됩니다.
# A 지역에서 생산된 제품을 B 지역에서 판매하려면 A 지역에서 B 지역까지의 운송비가 추가됩니다. 그런데 B 지역이 A 지역에서 구매한 제품을 다시 C 지역에게 판매한다면 C 지역은 생산자가격에서 A에서 B, B에서 C 두 번의 운송 가격을 더하여 판매하게 됩니다.
# 운송 단계를 줄여 자원 절약을 권장하려는 정부는 최대한 운송을 적게 하는 지역에 표창장을
# 수여하려고 합니다.

# 예를 들어, 5곳의 지역이 있고, 1과 3, 1과 4, 2와 3, 3과 4, 4와 5 지역이 서로 교류를 하는 경우를 생각해봅시다.
# 1 지역에서는 2 지역까지 3 지역을 통해 2단계 만에, 3 지역까지 1단계, 4 지역까지 1단계, 5 지역까지 4 지역을 통해서 2단계 만에 갈 수 있습니다. 따라서, 운송 단계의 수는 2+1+1+2 = 6입니다.
# 2 지역에서는 1 지역까지 3 지역을 통해서 2단계 만에, 3 지역까지 1단계 만에, 4 지역까지 3 지역을 통해서 2단계 만에, 5 지역까지 3 지역과 4 지역을 통해서 3단계 만에 운송할 수 있습니다. 따라서, 운송 단계의 수는 2+1+2+3 = 8입니다.

# 어떤 나라의 지역의 수와 교류 관계가 입력으로 주어졌을 때, 운송 단계가 가장 적은 지역을 구하는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 지역의 수 정수 N과 교류 관계의 수 정수 M을 입력합니다.
# (2 ≤ N ≤ 20)(1 ≤ M ≤ 400)
# 둘째 줄부터 M개의 줄에는 교류 관계를 입력합니다. 교류 관계는 정수 A와 B로 이루어져 있으며, A와 B가 교류한다는 뜻입니다. A와 B가 교류 관계면, B와 A도 교류하며, A와 B가 같은 경우는 없습니다.
# 교류 관계는 중복되어 들어올 수도 있으며, 교류 관계가 하나도 없는 지역은 없습니다. 또, 모든 지역은 교류 관계로 연결되어 있습니다
# [출력]
# 교류 관계의 수가 가장 작은 지역을 출력합니다. 그런 지역이 여러 곳일 경우에는 번호가 가장 작은 지역을 출력합니다.

# [입력 예시]
# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2
# [출력 예시]
# 3

from collections import deque

INF = 9999999   # 거리 무한대 
def resource_saving_bfs(graph,num):
    area = INF  # 최단경로 지역 초기값은 = 무한대
    d_sum = INF # 최단거리 초기값도 = 무한대
    
    # n개의 지역에 대해서, 최단경로를 전부 구해본다.
    i = 0
    while i < num:  
        
        # 매 차례 거리(d), 방문(v) 리스트를 초기화, 단, i(1~n)번째 지점의 d = 0, v = 1(방문함)으로 초기화하고 시작
        d = [INF] * (num+1)
        v = [0] * (num+1)
        d[i+1] = 0
        v[i+1] = 1

        queue = deque()
        queue.append(i+1)   # 큐에, i번째 지역(정점) 넣고 시작
        while queue:
            pop_area = queue.popleft()
            for j in range(1,num+1):
                if graph[pop_area][j] == 1:     # i번째 지역이랑, 인접한 지역이고
                    if v[j] == 0 and d[pop_area] + 1 < d[j]:    # 아직 방문한적없는 지역이고, i번째지역 d + 1 거리합보다, 최근 거리가 작아진다면
                        queue.append(j)         # 큐에 그 지역(정점)정보 넣고
                        d[j] = d[pop_area] + 1  # d(거리) 업데이트해주고
                        v[j] = 1    # v(방문) 방문했음으로 업데이트

        if sum(d[1:]) < d_sum:  # i번째지점에 대해, 최단경로 다 구해보고, 그 합이, 최근 가장 짧은 거리의 합보다 작으면
            d_sum = sum(d[1:])  # 최단거리 업데이트
            area = i+1  # 그때 지점(정점)정보도 업데이트
        i += 1

    return area


if __name__ == '__main__':
    n,m = map(int,input().split())
    graph = [[0]*(n+1) for _ in range(n+1)]     # n*n 으로 받지만, 인덱스 편의상 (n+1) *(n+1)로 인접행렬 만듦
    for _ in range(m):
        i,j = map(int,input().split())
        graph[i][j] = 1
        graph[j][i] = 1

    print(resource_saving_bfs(graph,n))
        

# # 아이디어
# - 각 생산지역이 정점이고, 두 생산지점사이의 운송비가 가중치(이문제에서는, 항상 인접한 두 생산지점 사이의 가중치는 = 1)이다.
# - 각 지점에서, 생성되는 가중그래프의 가중치합은 다를 수 있으므로, n개의 지점이 있다면, (1~n)개의 지점에서 운송을 할 경우를 전부 진행해서, "가장 짧은 운송비(가중치)"를 가지게 되는 지역을 뽑아내야한다.

# # 결과
# - 100

# # 질문거리
# - 각 지역(정점)마다 인접한 지역(정점)이 있는 것을 찾을 때, "인접행렬"을 사용했는데, 이럴 경우, n이 커질경우 인접한 정점을 찾는데 "시간초과"가 발생할 수 있다고 생각하는데
# - 이렇게, 한 정점으로부터, 인접한 다른 정점을 찾는데, "인접리스트"형식으로, 구현하는 것이, 일반적인 코딩테스트 문제에서, 시간초과에 대한 문제를 고려하지 않아도 되는 것인지 ?


