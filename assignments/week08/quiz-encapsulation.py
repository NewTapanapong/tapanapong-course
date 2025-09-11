"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width
    def getArea(self):
        return self.__lenght * self.__width
    def getPerimeter(self):
        return 2 * (self.__lenght + self.__width)
    def isSquare(self):
        if self.__lenght == self.__width:
            return True
        else:
            return False
        
check = Rectangle(5,5)
print(f"Area of check = {check.getArea()}")
print(f"Perimeter of check = {check.getPerimeter()}")

if check.isSquare():
    print("check is square")
else:
    print("Perimeter is not square")

check.getArea()
check.getPerimeter()
check.isSquare()
print(check.isSquare())