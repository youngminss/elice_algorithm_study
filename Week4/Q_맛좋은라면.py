# [투 포인터] 맛 좋은 라면

# 라면 회사에서 일하는 캐터필러는 라면 스프를 개발하고 있습니다. 회사에는 라면 맛을 내기 위한 다양한 종류의 조미료를 가지고 있습니다.
# 각 조미료에는 그 조미료의 매운 정도를 나타내는 하나의 정수가 주어져 있습니다. 라면을 맵게 만드는 분말의 매움 수치는 1부터 1,000,000까지의 양의 정수로 나타내고, 매운맛을 중화시켜주는 분말의 매움 수치는 -1부터 -1,000,000까지의 음의 정수로 나타냅니다.
# 같은 양의 두 조미료를 혼합한 분말의 매운 정도는 두 분말의 매움 수치를 더한 값과 같습니다. 캐터필러는 같은 양의 두 조미료를 사용하여 매운 정도가 0에 가장 가까운 분말을 만들려고 합니다.
# 예를 들어, 주어진 분말들의 매움 수치가 [-74, -30, -5, 10, 75]인 경우에 매움 수치가 -74인 분말과 75인 분말을 혼합한 매움 1의 분말을 만들 수 있고, 이 분말이 만들 수 있는 분말 중 가장 0에 가까운 매움 정도를 가진 분말입니다.
# 캐터필러가 사용할 수 있는 분말들의 매움 수치가 정렬된 순서로 주어졌을 때, 이 중 두 개의 서로 다른 분말을 혼합하여 매움 정도가 0에 가장 가까운 분말을 만들어내는 두 분말을 찾아내는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에는 전체 분말의 수 정수 N을 입력합니다.
# (2<=N<=400)
# 둘째 줄에는 분말의 매운 정도를 나타내는 N개의 정수를 공백을 두고 오름차순으로 입력하며, 이 수들은 모두 -1,000,000 이상 1,000,000 이하입니다. N개의 분말의 매움 수치는 모두 서로 다르고, 양수나 음수만으로 입력이 주어지는 경우도 있을 수 있습니다.
# [출력]
# 매운 정도가 0에 가장 가까운 분말을 만들어내는 두 분말의 매움 수치를 출력합니다.
# (출력해야 하는 두 분말은 매움 수치를 오름차순으로 출력합니다.)
# (매운 정도가 0에 가장 가까운 분말을 만들어내는 경우가 두 개 이상일 경우에는 그 중 절댓값의 합이 더 큰 경우를 출력합니다.)

# [입력 예시]
# 5
# -74 -30 -5 10 75
# [출력 예시]
# -74 75

def solution():
    n = int(input())
    datas = list(map(int,input().split()))

    l = 0
    r = len(datas) - 1
    less = 2000000

    while l < r:
        
        if abs(datas[l] + datas[r]) < less:
            pl = l
            pr = r
            less = abs(datas[l] + datas[r])
        elif abs(datas[l] + datas[r]) == less :
            if (abs(datas[l]) + abs(datas[r])) > (abs(datas[pl]) + abs(datas[pr])):
                pl = l
                pr = r

        if abs(datas[l+1] + datas[r]) < abs(datas[l] + datas[r-1]): l += 1
        else:  r -= 1

    print(datas[pl],datas[pr])
    
if __name__ == '__main__':
    solution()


# # 아이디어
# - 오름차순으로, 맵기 정도가 정렬이 되어 있는 상태이다.
# - 그럼 시작은, 맨 왼쪽과, 맨 끝쪽에서 시작하면, 주어진 맵기 정도들 중에서는 맵기의 절대값이 가장 작을 것이다.
# - 결과적으로, 양 쪽 끝 인덱스부터 시작해서, 가운데로 인덱스를 좁히면서, l 과 r이 교차 하기 전까지 탐색을 하며, 진행한다.
# - 한 가지 더 고려할 점은, 인덱싱을 하다, 어쩌다, 최근까지 가장 0에 가까울때의 l,r 값과 방금, l,r이 다른데, 절대값은 값을 경우가 있을 수 있다.
# - 그 때는, l,r 에 각각에 대해, 절대값의 합이 더 큰, 경우를, l, r로 설정할 수 있도록한다.
# - 그런 것이 아닌, 단순히 인덱스를 옮겨야 하는 경우는, l+1 을 했을 경우의 절대값과 r-1 을 했을 경우, 절대값이 더 작은 경우의 방향으로, 인덱싱을 한다.

# # 결과
# 100

# # 질문
# - 지금 내가 생각한, 인덱스 이동 방향을 결정할 때, 정당한 근거가 맞는가 ?
# - 인덱스를 꼭 (l+1) 혹은 (r-1) 로만 인덱싱해야 하나 ? 몇 칸씩 뛰어넘으면 안되는 것인가 ?
