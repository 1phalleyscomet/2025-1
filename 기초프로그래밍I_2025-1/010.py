import random
lottery_num=random.sample(range(1,45+1),6)
print(lottery_num)


import random

def game():
    answer_num=random.randint(1,100+1)

    while True:
        i=int(input("숫자입력>"))

        if i <answer_num:
            print("UP")
        elif i > answer_num:
            print("DOWN")
        else:
            print("RIGHT!")
            break

while True:
    game()
    retry=input("다시 하시겠습니까?(y/n):")
    if retry.lower() == 'y':
        continue
    else:
        print("게임을 종료합니다.")
        break
   

