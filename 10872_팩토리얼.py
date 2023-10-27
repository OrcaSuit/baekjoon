# N! (팩토리얼)을 계산하는 함수
def factorial(n):
    if n == 0:
        print("끝!")
        return 1
    else:
        print(f"{n}팩토리얼...")
        return n * factorial(n-1)

def factorial_use_for(n):
    output = 1
    for i in range(1, n +1):
        output *=i
    return output

# 정수 N을 입력 받음
N = int(input())

# N!을 계산하여 출력
print(factorial(N))
