import sys

def calculate():

    a, b = map(int, sys.stdin.readline().split())

    # 연산
    print(a+b)
    print(a-b)
    print(a*b)
    print(int(a/b))
    print(a%b)

# 함수 호출
calculate()
