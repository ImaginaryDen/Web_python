import math

class Sphere:
	def __init__(self, r = 1, x = 0, y = 0, z = 0):
		self.r = r
		self.x = x
		self.y = y
		self.z = z
	def get_volume(self):
		return (4 * math.pi * self.r ** 3) / 3
	def get_square_(self):
		return 4 * math.pi * self.r ** 2
	def get_radius_(self):
		return self.r
	def get_centre_(self):
		return tuple(self.x, self.y, self.z)
	def set_radius_(self, r):
		self.r = r
	def set_center(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def is_point_inside(self, x, y, z):
		return ((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2) < self.r **2

ob = Sphere(2)
print(ob.is_point_inside(0, 1, 0))