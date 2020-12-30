# 생수통

# 엘리스 샘물은 물을 담아 판매하기 위해 생수통을 외부 업체로부터 구매하려고 합니다. 구매하는 방법은 다음과 같습니다.
# 엘리스 샘물은 외부 업체가 제시한 세 종류의 물통과 두 종류의 뚜껑을 적절히 고르고 생수통을 만들어 달라고 요청을 합니다. 그러면 외부 업체가 물통과 뚜껑을 결합하고 재료비(뚜껑 가격+물통 가격)에서 10원을 추가해 엘리스 샘물에 생수통 하나를 판매합니다.
# 엘리스 생수통의 가격이 최소가 되도록 하고 싶습니다. 각 물통과 뚜껑의 가격을 줬을 때 생수통 한 개 가격의 최솟값을 출력하는 프로그램을 작성하세요.

# [입력]
# 첫 번째 줄부터 세 개의 물통의 가격을 한 줄씩, 두 개의 뚜껑 가격 두 줄을 입력합니다.
# ※물통의 가격은 100원부터 500원까지이고 뚜껑의 가격은 20원부터 80원까지입니다.

# [출력]
# 첫 번째 줄에 엘리스 샘물이 구매할 생수통 한 개 가격의 최솟값을 출력합니다.

# [Code]
bottle = [0] * 3
lid = [0] * 2

for i in range(3):
    bottle[i] = int(input())
for i in range(2):
    lid[i] = int(input())
bottle.sort()
lid.sort()

print(bottle[0] + lid[0] + 10)