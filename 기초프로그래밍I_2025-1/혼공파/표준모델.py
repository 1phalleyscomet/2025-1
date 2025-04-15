module import  모듈이름
import math math 모듈
math. <자동완성 기능
import math
math.sin(1)
math.floor(2.5) 내림
math.ceil(2.5) 올림
log(x[. base]
    )
반올림
round()

from 구문
from 모듈이름 import 가져오고싶은 변수, 함수
from math import sin,cos
cos(1)
모두 가져오기
from nath import *

as구문
import 모듈 as 사용하고싶은 식별자
import math as m
m.sin(1)

random 모듈
import random
print("random 모듈")
print("-rand():",random.random())#random()-0.0<=x<1.0사이의 float 리턴
print("uniform(10,20):",random.uniform(10,20)) #uniform(min,max)-지정한범위의 int 리턴
#randrange()-지정한 범위의 int 리턴
random.randrange(10)
#randrange(max)-0부터 max사이 값 리턴
#randrange(min,max)
random.choice([1,2,3])#choice(list)-리스트 내부 요소 랜덤 선택
random.shuffle([1,2,3])#shuffle(list)-리스트 내부 요소 랜덤 섞기
random.sample([1,2,3,4,5],k=2)#sample(list,k=number)-리스트의 요소 중 k개 선택
##모듈이름 파일 이름 동일하게 쓰기 x ex)random.py
from time import random,randrange, choice

sys 모듈
import sys
print(sys.argv) #명령 매개변수 출력
print("---")
print("getwindowsversion:()",sys.getwindowsversion())
print(sys.copyright)
print(sys.version)
sys.exit()

os 모듈
import os 
print("현 운영체제",os.name)
print("현제 폴더",os.getcwd())
print("현재 폴더 내부 요소",os.listdir())

#폴더 생성 후 제거 (폴더가 비어있을 때만 제거 가능)
os.mkdir("hello")
os,rmdir("hello")

#파일 생성 후 파일이름변경
with open("original.txt","w") as file:
    file.write("hello")
os.rename("original.txt","new.txt")
os.remove("new.txt")
os.system("dir")#시스템 명령어 실행

datetime 모듈
import datetime

print("현재시각출력")
now=datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
#시간을 포맷에 맞춰 출력
output_a=now.strftime("%Y.%n.%d.%H:%M:%S")
output_c=now.strftime("%Y{} %m{} %d{}").format(*"년월일")
#문자열, 리스트 앞 * -요소 하나하나가 매개변수로 지정

import datetime
now=datetime.datetime.now()

#시간 더하기
after=now + datetime.timedelta(\
    weeks=1,\
    days=1,\
    hours=1 )

#시간 요소 교체
output=now.replace(year=(now.year +1))

time 모듈
import time
print("5초 정지")
time.sleep(5)#코드 진행 5초 정지 후 진행
print("프로그램 종료")

ullib 모듈
from urllib import request

target=request.urlopen("https://google.com")
output=target.read()
print(output)