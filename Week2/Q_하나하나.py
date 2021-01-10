# [문자열] 하나하나

# 엘리스는 클로버 대학에서 석사 과정을 밟고 있습니다.
# 논문은 ‘일상생활에서 가장 많이 쓰이는 문자는 무엇인가?’를 주제로 작성하려고 합니다.
# 논문을 쓰기 위해 문장에 있는 대소문자들을 하나하나 센 뒤 문장에서 가장 많은 알파벳을 골라내야 합니다.
# 엘리스를 도와 문장이 주어지면 가장 많은 문자를 출력하는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 알파벳 대소문자로 이루어진 단어를 입력합니다.
# (주어지는 단어의 길이는 1 이상 10,000 이하입니다.)
# [출력]
# 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력합니다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ‘?’를 출력합니다

# [입력 예시 1]
# EliceIsGoodAndNicePerson
# [출력 예시 1]
# E
# [입력 예시 2]
# aaabbbcdefghijklmnopqrstuvwxyz
# [출력 예시 2]
# ?

def solution():
    datas = input()
    UpperAlpha = [0] * 26

    for data in datas:
        if 'A' <= data <= 'Z':
            UpperAlpha[ord(data) - 65] += 1
        if 'a' <= data <= 'z':
            UpperAlpha[ord(data) - 97] += 1

    sorted_UpperAlpha = UpperAlpha.copy()
    sorted_UpperAlpha.sort(reverse=True)

    if sorted_UpperAlpha[0] == sorted_UpperAlpha[1]:
        print('?')
    else:
        print(chr(65 + UpperAlpha.index(max(UpperAlpha))))

if __name__ == '__main__':
    solution()


# 아이디어
# - 일단, 검사할 문자열을 받는다.
# - 대문자(A~Z) or 소문자(a~z)가 등장하는 횟수를 담을 리스트 하나를 만든다. (이름은 UpperAlpha = 어차피 출력할 때 대문자라고 해서..)
# - 그리고, 일단 검사할 문자열을 끝까지 순회하면서, 카운팅한다.
# - 그리고나서, UpperAlpha를 복사해서, sort 해볼 sorted_UpperAlpha 리스트를 하나 만들었다. 그리고 이 리스트를 내림차순으로 정렬
# - 내림차순으로 정렬한 리스트에서, [0]번째 인덱스에 있는것이 등장횟수가 가장 큰건데, 가장 많이 등장한 횟수가 또 같은게 또 있을 수 있으니, 가장 가까운 [1]번째 인덱스의 값과 비교
# - 비교해서 같으면, 가장 많이 등장한 알파벳이 중복되는게 있는 것이니깐 => ? 출력
# - 아니면, 원래 UpperAlpha로 돌아와서, chr(65 + UpperAlpha.index(max(UpperAlpha)) 이용했다.
# - 이는, 먼저 UpperAlpha 안에서, 가장 많이 등장한 횟수에 해당하는 수를 max() 함수로 찾고
# - index() 함수로, 그 값이 존재하는 인덱스를 반환받아서 + 아스키코드값 65(A) 와 더한 알파벳 값을 출력하도록 했다.

# # 결과 [100]

# # 질문거리
# - 파이썬에서 제공하는 max() 나 index()를 찾아보는데, 이 둘이 list 함수로 검색했을 때가 아니고, 문자열함수로 검색했을떄 나왔다.
# - 근데, 리스트에도 적용이 된거 같은데, 글을 포스팅한 사람이 잘못 알고있는건지, 아니면, 그냥 tuple을 제외한 Iterator자료형은 다 적용이 가능한건지 알고싶다.(찾아보면 되긴한데..)
# - 일단, 너무 어렵게 풀이를 한건가..싶기도 하다. 더 좋은 방법이 있으면 알고싶다.
