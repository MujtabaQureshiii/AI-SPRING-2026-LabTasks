import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

    def draw(self):
        pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line(Shape):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return 0

    def perimeter(self):
        return math.dist((self.p1.x, self.p1.y), (self.p2.x, self.p2.y))

    def draw(self):
        print(f"Line from ({self.p1.x},{self.p1.y}) to ({self.p2.x},{self.p2.y})")


class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def area(self):
        x1, y1 = self.points[0].x, self.points[0].y
        x2, y2 = self.points[1].x, self.points[1].y
        x3, y3 = self.points[2].x, self.points[2].y
        return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2

    def perimeter(self):
        return sum(math.dist((p.x, p.y), (self.points[(i+1)%3].x, self.points[(i+1)%3].y)) for i, p in enumerate(self.points))

    def draw(self):
        print("Triangle at points:", [(p.x, p.y) for p in self.points])

class Rectangle(Shape):
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self):
        print(f"Rectangle at ({self.top_left.x},{self.top_left.y}) width={self.width}, height={self.height}")


class Square(Rectangle):
    def __init__(self, top_left, side):
        super().__init__(top_left, side, side)

    def draw(self):
        print(f"Square at ({self.top_left.x},{self.top_left.y}) side={self.width}")


class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def draw(self):
        print(f"Circle at center ({self.center.x},{self.center.y}) radius={self.radius}")


class Quadrilateral(Shape):
    def __init__(self, points):
        self.points = points

    def area(self):
        return "Complex area"

    def perimeter(self):
        return sum(math.dist((p.x, p.y), (self.points[(i+1)%4].x, self.points[(i+1)%4].y)) for i, p in enumerate(self.points))

    def draw(self):
        print("Quadrilateral at points:", [(p.x, p.y) for p in self.points])


class Pentagon(Shape):
    def __init__(self, points):
        self.points = points

    def area(self):
        return "Complex area"

    def perimeter(self):
        return sum(math.dist((p.x, p.y), (self.points[(i+1)%5].x, self.points[(i+1)%5].y)) for i, p in enumerate(self.points))

    def draw(self):
        print("Pentagon at points:", [(p.x, p.y) for p in self.points])


p1 = Point(0, 0)
p2 = Point(4, 0)
p3 = Point(4, 3)
p4 = Point(0, 3)

shapes = [
    Line(p1, p2),
    Triangle(p1, p2, p3),
    Rectangle(p1, 4, 3),
    Square(p1, 5),
    Circle(Point(2, 2), 3),
    Quadrilateral([p1, p2, p3, p4]),
    Pentagon([Point(0,0), Point(2,1), Point(3,3), Point(1,4), Point(-1,2)])
]

for shape in shapes:
    shape.draw()
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    print()
