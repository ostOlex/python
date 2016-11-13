import math


class GeoFigure:
    def area(self, class_obj,result):
        print(class_obj.__name__ + ' area is: ' + str(result))

    def test_input_value(self, class_obj, value):
        user_input = raw_input('Enter the {0} of {1}:'.format(value, class_obj.__name__))
        if GeoFigure.is_value_number(self, user_input):
            if user_input >= 0:
                return user_input
            else:
                if user_input.lower() == 'exit':
                    return
                else:
                    print ("Invalid value.")
                    self.test_input_value(class_obj, value)
        elif user_input.lower() == 'exit':
            return
        else:
            print ("Invalid value.")
            self.test_input_value(class_obj, value)

    @staticmethod
    def is_value_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


class Triangle(GeoFigure):
    def __init__(self):
        self.base = GeoFigure().test_input_value(Triangle,'base')
        self.height = GeoFigure().test_input_value(Triangle, 'height')

    def area(self):
        result = 0.5 * float(self.base) * float(self.height)
        GeoFigure().area(Triangle, result)


class Rectangle(GeoFigure):
    def __init__(self):
        self.length = GeoFigure().test_input_value(Rectangle,'length')
        self.width = GeoFigure().test_input_value(Rectangle,'width')

    def area(self):
        area = float(self.length) * float(self.width)
        GeoFigure().area(Rectangle, area)


class Circle(GeoFigure):
    def __init__(self):
        self.radius =  GeoFigure().test_input_value(Circle,'radius')

    def area(self):
        area = 2 * math.pi * float(self.radius)
        GeoFigure().area(Circle, area)


def main():
    while True:
        user_input = raw_input(
            'Enter "Triangle", "Rectangle" or "Circle" to get the area. \nEnter "exit" to exit:')
        figures_mass = [Triangle, Rectangle, Circle]
        is_input_figure = False
        for figure in figures_mass:
            if user_input.lower() == figure.__name__.lower():
                figure().area()
                is_input_figure = True
                break

        if user_input.lower() == 'exit':
            break
        elif is_input_figure == False:
            print('Invalid data. Please try again')
        else:
            print('Invalid data. Please try again')


if __name__ == '__main__':
    main()
