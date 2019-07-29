from math import sqrt


def side_length(point1, point2):
    length = sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return length


class Triangle:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

        self.c1 = side_length(self.x1, self.x2)
        self.c2 = side_length(self.x2, self.x3)
        self.c3 = side_length(self.x3, self.x1)

        self.per = side_length(self.x1, self.x2) + side_length(self.x2, self.x3) + side_length(self.x3, self.x1)

        self.h = 2 * sqrt(self.per * 0.5 * (self.per * 0.5 - self.c1) * (self.per * 0.5 - self.c2) * (
                self.per * 0.5 - self.c3)) / self.c1

    def sides(self):

        # tr_sides = [self.c1, self.c2, self.c3]
        # return tr_sides
        return "side_1 = " + str(self.c1) +  " " + "side_2 = " + str(self.c2) + " " + "side_3 = " + str(self.c3)

    def perimeter(self):
        return "Perimeter = " + str(self.per)
    #
    def height(self):
        return "Triangle height = " + str(self.h)

    def square_triangle(self):
        return "Triangle square = " + str(self.c1 * self.h / 2)

triangle1 = Triangle([15, -23], [0, 24], [-9, -21])
print(triangle1.sides())
print(triangle1.perimeter())
print(triangle1.height())
print(triangle1.square_triangle())
def side_length(point1, point2):
    length = sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return length




class Trapezium:
    def __init__(self, x1, x2, x3, x4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4

        self.c1 = side_length(self.x1, self.x2)
        self.c2 = side_length(self.x2, self.x3)
        self.c3 = side_length(self.x3, self.x4)
        self.c4 = side_length(self.x4, self.x1)

       
        self.per = self.c1 + self.c2 + self.c3 + self.c4

       



    def trap_sides(self):

        return print("side_1 = " + str(self.c1), "side_2 = " + str(self.c2), "side_3 = " + str(self.c3), "side 4 = " + str(self.c4))

    def check_if_equal(self):

        if (self.c1 == self.c3 and self.c2 != self.c4) or (self.c1 != self.c3 and self.c2 == self.c4):
            print("Трапеция равнобедренная!")
        else:
            print("Трапеция не равнобедренная!")

    def perimeter(self):

        return "Perimeter = " + str(self.per)

trapezium1 = Trapezium([-2, -2], [-3, 1], [7, 7], [3, 1])
trapezium1.check_if_equal()
trapezium1.trap_sides()
print(trapezium1.perimeter())
# print(trapezium1.height())
# print(trapezium1.square_triangle())


