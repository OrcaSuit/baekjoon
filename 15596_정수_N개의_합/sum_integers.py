import random
import time
import sys


length = random.randint(1,3000000)
lst = [random.randint(0, 1000000) for _ in range(length)]

def solve(a: list) -> list:
    return sum(a)

start_cpu_time = time.process_time()
result = solve(lst)
end_cpu_time = time.process_time()

print(f"=========================================================")
print(f"합계: {result}")
print(f"리스트 길이: {length} 개 ")
print(f"리스트 크기: {sys.getsizeof(lst)} 바이트 ")
print(f"더하는데 걸린 시간: {end_cpu_time - start_cpu_time} 초")
print(f"=========================================================")

