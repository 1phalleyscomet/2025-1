def factorial():
    num=int(input("숫자를 입력하세요>"))
    result=1
    for num in range(1,num+1,1):
        result*=num
    print(result)

while True:
    factorial()
    retry=input("다시 하시겠습니까?(y/n):")
    if retry.lower() == 'y':
        continue
    else:
        print("종료합니다.")
    break

    