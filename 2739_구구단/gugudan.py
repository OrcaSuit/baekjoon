import sys

def calculate():

    number = int(sys.stdin.readline())
    count = 1

    for count in range(1, 10):
        print(f"{number} * {count} = {number*count}")
    
# 함수 호출A
calculate()
