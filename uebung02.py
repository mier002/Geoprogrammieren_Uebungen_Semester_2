#Aufgabe1
class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    # Addition
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __radd__(self, other):
        return Vector3(self.x + other, self.y + other, self.z + other)

    # Subtraktion
    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        else:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __rsub__(self, other):
        return Vector3(self.x - other, self.y - other, self.z - other)

    # Multiplikation (Vektor*Vektor*Vektor)
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __rmul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)
    
    def cross(self, other):
        return Vector3(self.y*other.z - self.z*other.y,
                       self.z*other.x - self.x*other.z,
                       self.x*other.y - self.y*other.x)

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    
    def normalize(self):
        return Vector3(self.x/((self.x**2 + self.y**2 + self.z**2)**0.5),
                       self.y/((self.x**2 + self.y**2 + self.z**2)**0.5),
                       self.z/((self.x**2 + self.y**2 + self.z**2)**0.5))

#------Test-und-Ausführung------
a = Vector3(3, 4, 2)
b = Vector3(2, 1, 0)


print(a)

#Multiplikation
c1 = a*b
c2 = 4*a
c3 = a*4
c4 = 7.25*b
c5 = b*7.25
print(c1, c2, c3, c4, c5)

#Skalar
d = a.dot(b)
print(d)

#Kreuzprodukt
e = a.cross(b)
print(e)

#Normalisierung
print(a.normalize())