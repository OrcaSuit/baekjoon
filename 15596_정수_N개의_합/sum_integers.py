import random
import sys
import timeit

def generate_random_list(min_length=1, max_length=3000000, max_value=1000000):
    length = random.randint(min_length, max_length)
    return [random.randint(0, max_value) for _ in range(length)]

def compute_sum_of_list(lst: list) -> int:
    return sum(lst)

def main():
    lst = generate_random_list()

    start_time = timeit.default_timer()
    result = compute_sum_of_list(lst)
    end_time = timeit.default_timer()

    print(f"=========================================================")
    print(f"합계: {result}")
    print(f"리스트 길이: {len(lst)} 개 ")
    print(f"리스트 크기: {sys.getsizeof(lst)} 바이트 ")
    print(f"더하는데 걸린 시간: {end_time - start_time} 초")
    print(f"=========================================================")

if __name__ == "__main__":
    main()
