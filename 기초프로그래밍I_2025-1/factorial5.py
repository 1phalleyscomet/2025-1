import numpy as np
import time

def factorial(n):
    return np.prod(np.arange(1,n+1,dtype=object))

if __name__ == "__main__":
    n = 10000
    start = time.monotonic()
    result = factorial(n)
    end = time.monotonic()

   
    print(f"Time taken: {end - start:.6f} seconds")