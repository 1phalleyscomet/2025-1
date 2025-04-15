def fibo(n):
    if n==1:
        return 1
    elif n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
while True:
    n=int(input("숫자를 입력하세요>"))
    for n in range(1,n+1,1):
          print(fibo(n))
    break