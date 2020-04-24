class Account:
    def __init__(self,money,save):
        self.__money = money
        self.__save = save

    def __withdraw__(self):
        return self.__money - self.__save

    def __save__(self):
        return self.__money + self.__save

    def __check__(self):
        return self.__money

a = Account(3,2)
print(a.__withdraw__())
print(a.__check__())
print(a.__save__())

class Student:
    def __init__(self,korean,english,math,name):
        self.__korean = korean
        self.__english = english
        self.__math = math
        self.__name = name

    def __average__(self):
        return (self.__korean + self.__math + self.__english)/3

    def __sum__(self):
        return self.__korean + self.__math + self.__english

b = Student(100,90,100,'Siva')
print(b.__average__())