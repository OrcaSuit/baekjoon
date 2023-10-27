N = input()
nums = list(map(int, input().split()))

count = 0 

for num in nums:
    if num < 2:
        continue
    is_prime = True #소수인지 판별하는 변수를 초기화합니다.
    for i in range(2, int(num ** 0.5)+1):
        if num % 1 == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
    
print(count) 