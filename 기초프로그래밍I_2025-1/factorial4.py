import time

def factorial(n):
    result=1
    i=1
    while i<=n: 
        result *=i
        i+=1
    return result

if __name__ == "__main__":
    n = 10000
    start = time.monotonic()
    result = factorial(n)
    end = time.monotonic()

   
    print(f"Time taken: {end - start:.6f} seconds")