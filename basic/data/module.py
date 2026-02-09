# 모듈
# 함수, 변수, 클래스를 모아 놓은 파이썬 파일
# math 모듈 전체 import
# import math
# import sys

# print(math.sqrt(16))
# print(math.sin(2))
# print(sys.builtin_module_names)  # 사용할 수 있는 기본 모듈

# math 모듈에서 사용할 함수만 가져오기
from math import sin, cos, floor, ceil

# 장점: 바로 부르기 가능
# print(sin(1))
# print(cos(1))

# from random import random, uniform, randrange, choice, shuffle, sample

# print(random())  # 0 < x <= 1
# print(uniform(10, 20))  # 10~20사이의 수를 float 수로 리턴
# print(randrange(10, 20))  # 10~20 사이의 수
# print(choice([1, 2, 3, 4, 5, 6, 7, 8]))  # 주어진 리스트 안에서 임의로 랜덤 선택
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# shuffle(list1)  # 섞기
# print(list1)
# print(sample(list1, 2))  # 원하는 요소 개수만큼 추출

# # 별칭 붙여서 사용
# import math as m

# print(m.ceil(3.14))
# print(m.sin(3))

# 커스텀 모듈 호출
# import prt

# prt.prt1()
# prt.prt2()

# import sum1

# print(sum1.add(5, 10005))

# number = sum1.number_input()
# print("둘레", sum1.get_circ(number))
# print("면적", sum1.get_area(number))

import calc

calc = calc.Calc(6, 5)
print(calc.add())
print(calc.sub())
print(calc.div())
print(calc.multi())
