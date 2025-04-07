def number():
    num=int(input("숫자를 입력하세요>"))
    print(str(num)*num)
    

while True:
    number()
    retry=input("다시 하시겠습니까?(y/n):")
    if retry.lower() == 'y':
        continue
    else:
        print("종료합니다.")
    break

