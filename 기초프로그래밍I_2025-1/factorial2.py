import time
import sys

sys.setrecursionlimit(11000)

def factorial(n):
    if n ==0 or n==1:
        return 1
    return n* factorial(n-1)

if __name__ == "__main__":
    n = 10000
    start = time.monotonic()
    result = factorial(n)
    end = time.monotonic()

   
    print(f"Time taken: {end - start:.6f} seconds")