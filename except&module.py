print(dir())

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    num1=int(input("첫 번째 숫자를 입력하세요 : "))
    num2=int(input("첫 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러")
except ZeroDivisionError as err:
    print(err)
except Exception as err: #다른 모든 에러
    print(err)
# if, raise로 에러 커스텀 가능.

import theater_module as mv
mv.price(3)
from theater_module import *
price(3)

#패키지는 모듈의 집합
import travel.thailand #방법1
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

from travel.thailand import ThailandPackage #방법 2
trip_to = ThailandPackage()
trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()



#위치 찾기는 import inspect, random하고 print(inspect.getfile(파일 이름))
#패키지 가져오려면 pypi.org 사이트 접속
#실행하고 맨 아래 줄에 pip list, install, uninstall 등으로 쓸 수 있음.
#dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
lst = [1,2,3]
print(dir(lst))

name = "Jim"
print(dir(name)) #str에 쓸 수 있는 함수