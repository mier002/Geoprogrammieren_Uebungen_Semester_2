# Aufgabe1
import math
class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

v = Vector3(2, 3, 6)
print("Länge =", v.len())


# Aufgabe 2a (Basis)
class WGS84Coord:
    def __init__(self, longitude=0.0, latitude=0.0):
       self._longitude = longitude
       self._latitude = latitude

    def _longitude (self, longitude):
       if longitude < -180 or longitude > 180:
           raise ValueError("Der Wert ist ungültig. Er muss zwischen [-180 und 180] liegen.")
       
    def _latitude(self, latitude):
        if latitude < -90 or latitude > 90:
            raise ValueError("Der Wert ist ungültig. Er muss zwischen [-90 und 90] liegen.") 
        
wert = WGS84Coord(10, 20)
wert2 = WGS84Coord(60, 50)
print("Longitude:", wert._longitude)
print("Latitude:", wert._latitude)


# Aufgabe 2b (Funktioniert nicht wie gewollt) --> Falsch
class WGS84Coord:
    def __init__(self, _longitude=0, _latitude=0):
       self._longitude = _longitude
       self._latitude = _latitude
       self.set_longitude
       self.set_latitude

    def get_longitude(self):
        return self._longitude
    
    def get_latitude(self):
        return self._latitude
    
    def set_longitude(self, longitude):
        if longitude < -180:
            print("Länge wird auf -180 gestzt, da der Bereich von [-180, 180] überschritten wurde.")
            self._longitude = -180
        elif longitude > 180:
            print("Länge wird auf 180 gestzt, da der Bereich von [-180, 180] überschritten wurde.")
            self._longitude = 180
        else:
            self._longitude = longitude

    def set_latitude(self, latitude):
        if latitude < -90:
            print("Breite wird auf -90 gestzt, da der Bereich von [-90, 90] überschritten wurde.")
            self._latitude = -90
        elif latitude > 90:
            print("Breite wird auf 90 gestzt, da der Bereich von [-90, 90] überschritten wurde.")
            self.latitude = 90
        else:
            self._latitude = latitude 

wert = WGS84Coord(200, 100)
wert2 = WGS84Coord(60, 50)
print("Longitude:", wert.get_longitude())
print("Latitude:", wert.get_latitude())


#Aufgabe 2c --> Falsch
class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
       self._longitude = longitude
       self._latitude = latitude

    def ausgabe1(self):
        print(f"Die Länge beträgt: {self._longitude}")

    def ausgabe2(self):
        print(f"Die Breite beträgt: {self._latitude}")

    def getLongitude(self):
        return self.longitude
    
    def getLatitude(self):
        return self.latitude
    
    def setLongitude(self, laenge):
        if laenge < -180 or laenge > 180:
            raise ValueError("Der Wert ist ungültig. Er muss zwischen [-180 und 180] liegen.")
        self._longitude = laenge

    def setLatitude(self, breite):
        if breite < -90 or breite > 90:
            raise ValueError("Der Wert ist ungültig. Er muss zwischen [-90 und 90] liegen.")
        self._latitude = breite

    laenge = property(getLongitude, setLongitude)
    breite = property(getLatitude, setLatitude)
    
wert = WGS84Coord(10, 20)
wert.ausgabe1()
wert.ausgabe2()

wert.laenge = 166
wert.breite = 66
wert.ausgabe1()
wert.ausgabe2()

print(wert._longitude)
print(wert._latitude)

