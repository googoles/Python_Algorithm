# private = 정보은닉 방식 class 의 attribute, method 에 대해 접근을 제어할 수 있는 기능
# private -> protected -> public
# private: private로 선언된 attribute, method는 해당 클래스에서만 접근 가능
# protected: protected 로 선언된 attribute, method는 해당 클래스 또는 해당 클래스를 상속받은 클래스에서만 접근가능
# public: public으로 선언된 attribute, method는 어떤 클래스라도 접근가능
# 파이썬은 기본적으로 public class

# protected는 해당 속성앞에 _ 봍여서 사용  일종의 경고표시

# private 는 attribute, method 앞에 __(double underscore)를 붙이면 된다.
# 실은 __을 붙이면 해당 이름이 해당 속성 또는 메소드 이름으로 변경되기 때문

# class Quadrangle:
#     def __init__(self, width, height, color):
#         self.__width = width
#         self.__height = height
#         self.__color = color
#
#     def get_area(self):
#         return self.__width * self.__height
#
#     def __set_area(self, width, height):
#         self.__width = width
#         self.__height = height
# square = Quadrangle(5,5,'black')
# print(dir(square))
# print(square.get_area())

'''
위 클래스, 객체를 기반으로 다음 코드 실행해보고 안되는 이유 생각해보기
print(square.__width)
square.__width = 10
square.__set_area(3, 3)
'''

class Circle:
    def __init__(self,radius,name):
        self.__radius = radius
        self.__name = name

    def get_name(self):
        return self.__name

    def get_area(self):
        return 3.14*self.__radius ** 2

circle = Circle(3,'dave')
print(circle.get_name(),circle.get_area())
