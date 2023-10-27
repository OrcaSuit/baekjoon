# 에라토스테네스의 체를 사용해 N까지의 모든 소수를 구하는 함수
def get_primes(N):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False
    return [x for x in range(N+1) if sieve[x]]  # 소수만 반환

# 테스트 케이스 개수 T를 입력 받음
T = int(input())

# 10,000 이하의 모든 소수를 미리 구함
primes = get_primes(10000)

# 소수인지 아닌지 빠르게 판별할 수 있는 딕셔너리를 만듦
is_prime = {prime: True for prime in primes}

# 각 테스트 케이스에 대해 실행
for _ in range(T):
    n = int(input())  # 짝수 n을 입력 받음
    
    a = b = n // 2  # a와 b를 n의 절반으로 초기화
    
    # a와 b가 둘 다 소수이고 합이 n이 될 때까지 반복
    while not (is_prime.get(a, False) and is_prime.get(b, False)):
        a -= 1  # a는 작아지고
        b += 1  # b는 커진다
        
    print(a, b)  # a와 b를 출력
