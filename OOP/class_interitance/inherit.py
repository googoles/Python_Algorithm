# 추상화 : 여러 클래스에 중복되는 속성 method를 하나의 기본 클래스로 작성하는 작업
# 상속 : 기본 클래스의 공통 기능을 물려받고, 다른 부분만 추가 또는 변경하는것
# 이때 기본 클래스는 부모클래스 Parent Super, Base class 라고 부름
# 기본 클래스 기능을 물려받는 클래스는 자식 클래스(또는 하위 클래스), child, sub, derived class라고 부름
# 코드 재사용이 가능,
# 부모클래스가 두개이상이면 다중상속이라고함

# class Figure:
#     def __init__(self,name,color):
#         self.__name = name
#         self.__color = color
#
# class Quadrangle(Figure):
#     def set_area(self,width,height):
#         self.__width = width
#         self.__height = height
#
#     def get_info(self):
#         print(self.__name, self.__color, self.__width, self.__height)
#
# # square = Quadrangle('dave', 'blue')
# # square.set_area(5, 5)
# # square.get_info()
#
# print(issubclass(Quadrangle,Figure)) # subclass 확인

# # 클래스 선언
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Student(Person):
#     def study(self):
#         print(self.name + " studies hard")
#
#
# class Employee(Person):
#     def work(self):
#         print(self.name + " works hard")
#
# student1 = Student("dave")
# employee1 = Employee('saveƒ®')
# print(student1.study())
# print(employee1.work())

# Method Override (메소드 재정의)
"""
부모클래스의 method를 자식 클래스에서 재정의
자식 클래스에서 부모 클래스 method를 재정의함
자식 클래스 객체에서는 재정의된
"""