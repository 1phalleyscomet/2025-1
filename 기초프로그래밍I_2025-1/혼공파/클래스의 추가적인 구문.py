'''
객체(인스턴스)가 어떤 클래스로 만들어졌는지 확인 -> isinstantce()
isinstantce(인스턴스,클래스)
'''

class Studnet:
    def __init__(self):
        pass

studnet=Studnet()
print(isinstance(studnet,Studnet))

#True
#type(student)==Studnet

class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass

Student=Studnet()

print(isinstance(studnet,Human))
#True
print(type(student)==Human)
#False

#__str__()함수
def __str__(self):
    return "{}\t{}\t{}".format(
        self.name
        self.get_sum(
        self.get_ave()
        )
    )

for student in studnets:
    print(str(student))

'''
클래스 변수 만들기
class 클래스명:
    클래스 변수=값
클래스 변수에 접근하기
클래서 명.변수 명
'''
'''
클래스 함수 만들기
class 클래스 명:
    @classmethod
    def 클래스 함수(cls,매개변수):
        pass
        
클래스 함수 호출
클래스 명.함수명(매개변수)
'''