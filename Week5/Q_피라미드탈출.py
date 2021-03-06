# [DP] 피라미드 탈출

# 삼각형 모양의 피라미드가 있습니다.
# 이 피라미드의 모든 방에는 숫자가 적혀있는데
# 이 숫자는 각 방을 통과하는 데 걸리는 시간을 의미합니다.
# 어느 날 피라미드를 방문한 여행객들이 꼭대기 층에 갇니습니다.
# 이들은 가장 아래층까지 모두 통과해야 피라미드를 탈출할 수 있으며, 아래층으로 내려갈 때는 현재 층에서 대각선 왼쪽 또는 대각선 오른쪽으로만 내려갈 수 있습니다.
# 그런데 심심했던 피라미드의 수호자 스핑크스는 모든 사람을 보내주긴 싫어서 조건을 내걸었습니다.
# “가장 느리게 탈출한 사람들만 집에 보내주겠다.”
# 탈출할 수 있는 사람들이 탈출에 걸릴 시간을 출력하는 프로그램을 작성하세요.
# (단, 모든 사람은 쉬지 않고 이동합니다.)

# [입력]
# 첫째 줄에 피라미드의 층수 N을 입력합니다.
# (1 <= N <= 100)
# 둘째 줄부터 N+1번째 줄까지 음수가 아닌 1000과 같거나 작은 정수로 이루어진 피라미드를 입력합니다.
# [출력]
# 탈출하는데 걸리는 최장 시간을 출력합니다.

# [입력 예시]
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
# => 실제 피라미드는 아래 모양이겠지
#         7
#       3   8
#     8   1   0
#   2   7   4   4
# 4   5   2   6   5
# [출력 예시]
# 30
# (7, 3, 8, 7, 5를 거치는 것이 정답입니다.)

def survive_pyramid(pyramid,n):

    dp = [[0]*i for i in range(1,n+1)]
    dp[0][0] = pyramid[0][0]

    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + pyramid[i][0]
        dp[i][i] = dp[i-1][i-1] + pyramid[i][i]
    
    for i in range(n):
        for j in range(i+1):
            if j != 0 and j != i:
                if dp[i-1][j-1] < dp[i-1][j]:
                    dp[i][j] = dp[i-1][j] + pyramid[i][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + pyramid[i][j]
    
    return max(dp[-1])

if __name__ == '__main__':
    n = int(input())
    pyramid = [list(map(int,input().split())) for _ in range(n)]
    
    print(survive_pyramid(pyramid,n))


# # 아이디어
# - 피라미드 꼭대기에서 내려갈 수 있는 방향은 1.왼쪽아래,2.오른쪽아래 2가지다.
# - 각, 방마다 통과할 수 있는 시간이있고, 맨 아래층까지 내려간다는 전제하에, 최적해는 "시간이 가장많이 걸리는 경로"인듯하다.
# - 그럼, 각 방마다, 양쪽에서 내려올 수 있는 방향 중, 시간이 더 오래걸리는 방향쪽의 시간과, 현재 내 방의 시간을 더해서 내려가는 식으로 풀이하면 어떻까 생각했다.
# - 그리고, 인덱싱 제어 문제가 하다보니 귀찮았는데, 생각해보니, 양쪽 바깥쪽 벽면은, 항상 왼쪽벽면은, 오른쪽 위의 시간 + 본인시간이고, 오른쪽 벽면은 왼쪽 위에 시간 + 본인시간이더라. 그래서, 가운데 부분을 제외하고, 먼저 전부 초기화시킨다.
# - 그리고나선, 가운데 부분은, 해당 위치에서, 왼쪽위와 오른쪽 위에서 내려오는 방법 중, 둘 중에 시간이 좀 더 걸려서 내려오는 방향의 시간 + 내 방의 시간을 해서, 모든 방에대해 DP를 진행하는 걸로 했다.

# # 결과
# 100

# # 질문거리
# - 이쯤되니, 많은 DP문제가 있겠지만, 지난주 문제중에, "스키"문제도 그렇고, "단방향"으로 진행되고, 뭔가 "최적해가 끝내 최대 or 최소값"을 구해야되는 DP문제는 방식이 비슷한거 같기도하고, 느낌이 대충 오는거 같다
# - 문제는, 그렇지 않은 문제들인데,,지금 드는 생각이 맞는건지 모르겠다.
