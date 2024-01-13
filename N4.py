import math

class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4/3) * math.pi * self.radius**3

    def get_square(self):
        return 4 * math.pi * self.radius**2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2)
        return distance < self.radius

sphere1 = Sphere(3, 1, 2, 3)

print("Радиус:", sphere1.get_radius())
print("Координаты центра:", sphere1.get_center())
print("Объем:", sphere1.get_volume())
print("Площадь поверхности:", sphere1.get_square())


sphere1.set_radius(5)
sphere1.set_center(-1, -2, -3)

print("Точка (-1, -2, -3) внутри сферы:", sphere1.is_point_inside(-1, -2, -3))
print("Точка (5, 5, 5) внутри сферы:", sphere1.is_point_inside(5, 5, 5))