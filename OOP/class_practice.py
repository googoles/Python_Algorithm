class Quadrangle:
    width = 0
    height = 0
    color = "black"

    def get_area(self):
        return self.width * self.height

    def set_area(self, data1, data2, data3):
        self.width = data1
        self.height = data2
        self.color = data3

square1 = Quadrangle()
square2 = Quadrangle()

square1.set_area(10,5,'red')
square2.set_area(7,7,'blue')

print(square1.get_area())
print(square2.get_area())