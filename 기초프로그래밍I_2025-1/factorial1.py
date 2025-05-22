import time

def factorial(n):
    result = 1
    for i in range(1,n+1,1):
        result *= i
    return result

if __name__ == "__main__":
    n = 10000
    start = time.monotonic()
    result = factorial(n)
    end = time.monotonic()

    
    print(f"Time taken: {end - start:.6f} seconds")

