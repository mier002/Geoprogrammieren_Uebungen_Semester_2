# Uebung 03
import math

#Punkt --------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Figur --------------------------------------------
class Figur:
    def __init__(self, name):
        self.name = name

    def umfang(self):
        return 0
    
    def __str__(self):
        return self.name

#Kreis --------------------------------------------
class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.M = mittelpunkt
        self.r = radius
    
    def umfang(self):
        return 2 * math.pi * self.r
    
    def __str__(self):
        return f"{self.name} M={self.M} r={self.r}"

k = Kreis(Point(2.3,4.2), 3.4)
print(k.name, k.umfang())


#Dreieck --------------------------------------------
class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__("Dreieck")
        self.a = a
        self.b = b
        self.c = c

    def umfang(self):
        ab = math.sqrt((self.a.x - self.b.x)**2 + (self.a.y - self.b.y)**2)
        bc = math.sqrt((self.b.x - self.c.x)**2 + (self.b.y - self.c.y)**2)
        ca = math.sqrt((self.c.x - self.a.x)**2 + (self.c.y - self.a.y)**2)
        return ab + bc + ca

    def __str__(self):
        return f"{self.name} {self.a}, {self.b}, {self.c}"

#Rechteck --------------------------------------------
class Rechteck(Figur):
    def __init__(self, a, c):
        super().__init__("Rechteck")
        self.a = a
        self.c = c

    def umfang(self):
        return 2 * (abs(self.a.x - self.c.x) + abs(self.a.y - self.c.y))
    
    def __str__(self):
        return f"{self.name} {self.a} - {self.c}"
        
#Polygone --------------------------------------------
class Polygon(Figur):
    def __init__(self, punkte):
        super().__init__("Rechteck")
        self.punkte = punkte
        
    def umfang(self):
        umfang = 0
        n = len(punkte)
        for i in range(n):
            x1, y1 = punkte[i]
            x2, y2 = punkte[(i+1) % n]
            umfang += math.sqrt((x2 -x1)**2 + (y2 - y1)**2)
        return umfang
    
    def __str__(self):
        punkte_str = ', '.join(str(punkte) for punkte in self.punkte)
        return f"{self.name} {punkte_str}"

punkte = [(0,0), (1,0), (1,1), (0,1)]


#Werte --------------------------------------------
K = Kreis((2.3, 4.2), 3.4)
D = Dreieck(Point(0, 0), Point(4, 0), Point(0, 3))
R = Rechteck(Point(0, 0), Point(10, 15))
P = Polygon([Point(0, 0), Point(4, 0), Point(4, 4), Point(0, 4)])


#Test Umfang --------------------------------------------
print(K)
print(D)
print(R)
print(P)