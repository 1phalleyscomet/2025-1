def rac_cal():
    w=float(input("넓이를 입력하세요>"))
    h=float(input("높이를 입력하세요>"))
    print(w*h)

while True:
    rac_cal()
    retry=input("다시 하시겠습니까?(y/n):")
    if retry.lower() == 'y':
        continue
    else:
        print("종료합니다.")
    break