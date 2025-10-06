class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y   

class Rectangle:
    def __init__(self, width: int, height: int, centerpoint: Point):
        self.width = width
        self.height = height
        self.point = centerpoint
    
    def compute_area(self, a=None, b=None):
        if a is not None and b is not None:
            return abs(a.x - b.x) * abs(a.y - b.y)
        else:
            return self.width * self.height

    def compute_perimeter(self, a=None, b=None):
        if a is not None and b is not None:
            return 2 * (abs(a.x - b.x) + abs(a.y - b.y))
        else:
            return 2 * (self.width + self.height)

Center_R1 = Point(1, 1)
R1 = Rectangle(3, 8, Center_R1)

print("Área desde atributos:", R1.compute_area())  # 15
print("Perímetro desde atributos:", R1.compute_perimeter())  # 16

p1 = Point(0, 0)
p2 = Point(3, 5)

print("Área desde puntos:", R1.compute_area(p1, p2))  # 15
print("Perímetro desde puntos:", R1.compute_perimeter(p1, p2))  # 16

class Square(Rectangle):
    def __init__(self, width, height, centerpoint):
        super().__init__(width, height, centerpoint)

    def compute_interference_point(self, a):
        if a.x <= 