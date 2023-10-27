import time
import sys

sys.setrecursionlimit(10**6)

def f(n, memo):
    if memo[n] is not None:
        return memo[n]
    
    memo[n] = f(n-1, memo) + f(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    n = int(input())
    
    start_time = time.time()
    
    memo = [0, 1] + [None] * (n - 1)
    print(f(n, memo))
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
