# [큐] 파자마 파티에는 게임이 빠지면 안 돼

# 하트 여왕은 파자마 파티를 열었습니다. 파자마 파티는 잠옷을 입고 밤새우면서 노는 것을 말합니다. 하트 여왕의 파자마 파티에는 총 N명의 친구가 왔습니다. 그리고 하트 여왕은 친구들과 게임을 하려고 합니다.
# 친구들 N명은 1번부터 N 번까지 시계방향으로 원형으로 앉았습니다. 1번부터 한 명씩 시계방향으로 1, 2, … , K까지 셉니다. K를 말하는 사람은 원에서 나갑니다. 그 후에는 다음 자리에 앉아있는 사람이 1부터 다시 셉니다. 하트 여왕도 이 게임에 M 번으로 참가합니다. 하트 여왕은 자기가 몇 번째로 원에서 나가는지 궁금해졌습니다.
# N, K, M이 주어졌을 때, 하트 여왕이 몇 번째로 원에서 나가는지 알아내는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 N, K, M을 입력합니다.
# N과 K는 5,000,000보다 작거나 같은 자연수이고, M은 N보다 작거나 같습니다.
# [출력]
# 첫째 줄에 하트 여왕이 몇 번째로 원에서 나가는지 출력합니다.

# [입력 예시]
# 10 5 3
# [출력 예시]
# 10

def solution():
    n,k,m = map(int,input().split())
    datas = [ i for i in range(1,n+1)]

    result = 0
    index = -1    
    for _ in range(len(datas)):
        index = (index + k) % len(datas)
        if datas.pop(index) == m :
            result += 1
            break
        else:
            result += 1
            index -= 1
    print(result)

if __name__ == '__main__':
    solution()


# 아이디어
# - (1~N) 까지의 번호를 가진 사람들이 "원형" 으로 둘러 앉아있고, 3,6,9 게임처럼 매번 k 번 후에 앉아있는 사람은 out !
# - 그럼, 문제는 매번 사람이 탈락할때마다, 전체 n이 1 씩 감소하면서, 결국 "전체 크기가 1씩 줄어든다."
# - 원형 큐를 사용해야되고, 그에 필요한, 매 차례, "(기존index + k) % (매차례 전체크기) = 매 차례 삭제될 위치에 인덱스"를 생각해내야한다.
# - 나머지는, 그 인덱스에 위차한, 리스트의 요소를 pop()시키고, 그 pop한 데이터가 m과 같으면, 반복문 탈출, (맞을때까지 반복)

# # 질문거리
# - "큐"문제라고 했는데, 전형적인 "원형큐" 문제가 맞는지 궁금하다.
