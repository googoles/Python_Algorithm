class Quadrangle:
    def __init__(self,width,height,color):
        self.width = width
        self.height = height
        self.color = color

    def __del__(self):
        print("Quadrangle object is deleted")

square = Quadrangle(5,5,'black')
# print(square.width)
# del square
# print(square.width)
    # width = 0
    # height = 0
    # color = "black"

    # 클래스에서 self.attribute명을 사용할 수는 없다.

