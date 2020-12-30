# 숫자 나라 특허 전쟁

# 숫자 나라에는 숫자 3을 상징하는 삼삼 가문과 숫자 5를 상징하는 오오 가문이 있었습니다.
# 두 가문은 모든 사람이 자신들의 가문을 상징하는 숫자들을 마구잡이로 사용하는 것이 불만이었습니다. 그래서 두 가문은 각각 자신들의 숫자에 특허를 내기로 하였습니다.
# 삼삼 가문은 모든 3의 배수에 특허를 내고 오오 가문은 모든 5의 배수에 특허를 내었습니다. 이후 사람들은 3의 배수와 5의 배수를 마음대로 쓸 수 없게 되었습니다.
# 사람들은 마음대로 쓸 수 없는 수의 크기가 얼마나 되는지 알아보기로 하였습니다.
# 예를 들어, 10보다 작은 자연수라면 3, 5, 6, 9에 특허가 걸려서 사용하지 못하고, 이것을 모두 더하면 그 크기는 23입니다.
# 그러면 N보다 작은 자연수 중에서 특허가 걸려있는 수를 모두 더한 크기를 구하는 프로그램을 작성하세요.

# [입력]
# 첫째 줄에 자연수 N을 입력합니다.
# (1<= N <= 100,000)

# [출력]
# N보다 작은 자연수 중에서 특허가 걸려 마음대로 쓸 수 없는 수들의 합을 출력합니다.

# [입력 예시]
# 10

# [출력 예시]
# 23

# [Code]
n = int(input())
result = 0

for i in range(3,n):
    if i % 3 == 0 and i % 5 == 0:
        result += i
    elif i % 3 == 0:
        result += i
    elif i % 5 == 0:
        result += i

print(result)