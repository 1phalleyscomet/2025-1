import time
import math 

def factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    n = 10000
    start = time.monotonic()
    result = factorial(n)
    end = time.monotonic()

   
    print(f"Time taken: {end - start:.6f} seconds")