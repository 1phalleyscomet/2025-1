import random
def game():
    lottery_num=random.sample(range(1,45+1),6)
    print(lottery_num)


while True:
    game()
    retry=input("다시 하시겠습니까?(y/n):")
    if retry.lower() == 'y':
        continue
    else:
        print("게임을 종료합니다.")
        break
   



