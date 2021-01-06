# [K 번 곱하기]
# 자연수 N과 K가 있습니다. 심심한 체셔는 1부터 N까지의 수를 K 번씩 곱한 후 더하려고 합니다.

# 식으로 나타내면 다음과 같습니다.

# 1^K + 2^K + … + + N^K1 
# K
#  +2 
# K
#  +…++N 
# K
 
# 계산 결과를 1,000,000,009로 나눈 수를 출력하는 프로그램을 작성하세요.

# [입력]
# 자연수 N과 K를 입력합니다.
# (1<=N<=1,000,000,000)
# (1<=K<=50)

# [출력]
# 1^K + 2^K + … + + N^K1 를 1,000,000,009로 나눈 나머지를 출력합니다.

# [입력 예시]
# 4 2
# [출력 예시]
# 30

# [Code] 60점
n, k = map(int,input().split())
sum_num = 0

if n % 2 == 0:
    for i in range(1, n//2 + 1):
        sum_num += (i ** k) + ((n-(i-1)) ** k)
else :
    for i in range(1, n//2) :
        sum_num += (i ** k) + ((n-(i-1)) ** k)
    sum_num += (n//2 + 1) ** k
print(sum_num % 1000000009)


# 피드백

# 이 문제는 분류는 "수학" 문제인데, (1~N)까지의 K승의 합을 구하는 "파울하버의 공식" 이란
# 수학적 개념을 알고 있어야한다....
# 링크 : https://namu.wiki/w/%ED%8C%8C%EC%9A%B8%ED%95%98%EB%B2%84%EC%9D%98%20%EA%B3%B5%EC%8B%9D
# 파울하버의 공식에서 주어지는 일반식을 코드로 옮기면 되는 문제이긴하다.

import math
PRIME = 1000000009

def combination(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
    
def mod_power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a % PRIME
    x = mod_power(a, b//2)
    if b % 2 == 1:
        return a*((x*x) % PRIME) % PRIME
    return (x*x) % PRIME
    
def main():
    inp = list(map(int, input().split()))
    N = inp[0]
    K = inp[1]
    k_sums = [0] * (K+1)
    k_sums[0] = N
    for k in range(1, K+1):
        k_sums[k] = mod_power(N+1, k+1) - 1
        #print(k_sums[k])
        for p in range(0, k):
            k_sums[k] -= combination(k+1, p) * k_sums[p] % PRIME
        k_sums[k] *= mod_power(k+1, PRIME-2)
        k_sums[k] %= PRIME
    print(int(k_sums[K]) % PRIME)
if __name__ == "__main__":
    main()