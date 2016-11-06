import math


class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = 0.5 * float(self.base) * float(self.height)
        print("Triangle area is: " + str(area))

class Rectangle():
    def __init__(self, length, width ):
        self.length = length
        self.width = width

    def area(self):
        area = float(self.length) * float(self.width)
        print("Rectangle area is: " + str(area))

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 2 * math.pi * float(self.radius)
        print("Circle area is: " + str(area))

def main():
    while True:
        userInput = raw_input(
            'Enter "Triangle", "Rectangle" or "Circle" to get the area. \nEnter "exit" to exit:')
        if ((userInput.lower() == 'triangle') | (userInput.lower() == 'rectangle') | (userInput.lower() == 'circle')):
            result_class = ''
            if (userInput.lower() == 'triangle'):
                userInput = raw_input('Enter the base of triangle:')
                base = userInput
                userInput = raw_input('Enter the height of triangle:')
                height = userInput
                result_class = Triangle(base,height)
            elif (userInput.lower() == 'rectangle'):
                userInput = raw_input('Enter the length of rectangle:')
                length = userInput
                userInput = raw_input('Enter the width of rectangle:')
                width = userInput
                result_class = Rectangle(length, width)
            elif (userInput.lower() == 'circle'):
                userInput = raw_input('Enter the radius of circle:')
                result_class = Circle(userInput)
            result_class.area()
        elif (userInput.lower() == 'exit'):
            break
        else:
            print('Invalid data. Please try again')


if __name__ == '__main__':
    main()
