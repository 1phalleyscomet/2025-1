#파이썬 파일 생성 후 외부에서 읽어들이기

#module file
PI=3.14
def number_input():
    output = input("숫자입력>")
    return float(output)
def get_circumference(radius):
    return 2 *PI * radius

def get_area(radius):
    return PI * radius * radius

#main file
import module file as test
radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_area(radius))

#복잡하고 구조화된 모듈->package 기능 사용
#프로그램 진입점 entry point/main
import module file 
print("#메인의 __name__ 출력하기 ")
print(__name__)
print()

