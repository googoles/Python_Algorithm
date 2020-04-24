import math
class Figure:

    def __init__(self,length, name):
        self.length = length
        self.name = name

    def get_area(self):
        return (math.sqrt(3)/2) * self.length**2

    def get_name(self):
        return self.name

    def __del__(self):
        print("Object is deleted")

square = Figure(10,'dave')
print(square.get_area(),square.get_name())