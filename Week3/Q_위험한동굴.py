# [순열] 위험한 동굴

# N명의 탐험가는 동굴에 들어가기에 앞서 들어가는 순서를 정하려고 합니다. 이때 동굴에 들어가는 순서의 가짓수를 출력하는 프로그램을 작성하세요.
# (※ 탐험가는 1번부터 N 번까지 번호가 붙어있습니다.)

# [입력]
# 첫 번째 줄에 탐험가의 인원수인 자연수 N을 입력합니다.
# (1≤N≤6)
# [출력]
# 첫 번째 줄에 탐험가들이 동굴에 들어가는 순서를 공백을 기준으로 한 줄씩 전부 출력합니다.
# ※ 출력은 오름차순으로 정렬해 출력합니다.

# [입력 예시]
# 2
# [출력 예시]
# 1 2
# 2 1

def solution():
    from itertools import permutations

    n = int(input())
    Explorers = [i for i in range(1,n+1)]
    datas = permutations(Explorers,n)
    print(type(datas))
    for data in datas:
        for Explorer_number in data:
            print(Explorer_number,end=" ")
        print()

if __name__ == '__main__':
    solution()


# 아이디어
# - 최대 1 ~ 6 번까지의 모험가가, 들어갈 수 있는 경우의 수, (즉, 순열)를 구하라는 문제 (중복 X)
# - 파이썬에서 기본적으로 제공하는 itertools 라이브러리에 permutations(순열) 라이브러리를 알고 있다면 쉽게 풀 수 있다.
# - 자동으로, 오름차순이고, class 'itertools.permutations', 즉 클래스를 반환한다.
# - 사용시는, 클래스 덩어리를, 반복문을 통해서, 사용한다.

# # 결과
# [100]

# # 질문거리
# 만약에, permutations 을 몰랐다면, 임의의 n에 대해서, 6중 포문을 만들어 놔야하나 ?


