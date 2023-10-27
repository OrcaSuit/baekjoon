import time
import sys
sys.setrecursionlimit(10**6)
                      
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

if __name__ == '__main__':
    n = int(input())
    
    start_time = time.time()
    
    print(f(n))
    
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")
