class Taisnsturis:
    def __init__(self, x, y):
        print(f"Izveidots taisnstūris ar malām {x} un {y}")
        self.a = x
        self.b = y

    def laukums(self):
        return self.a * self.b

    def perimetrs(self):
        return 2 * (self.a + self.b)
    
# t = Taisnsturis(7, 5)
# print("Taisnstūra mala a: ", t.a)
# print("Taisnstūra mala b: ", t.b)
# print("Taisnstūra laukums: ", t.laukums())
# print("Taisnstūra perimetrs: ", t.perimetrs())

class TaisnlenkaTrijsturis:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def hipotenuza(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5
    
    def perimetrs(self):
        return self.a + self.b + self.hipotenuza()
    
# trijsturis1 = TaisnlenkaTrijsturis(6, 8)
# print(trijsturis1.hipotenuza())
# print(TaisnlenkaTrijsturis.hipotenuza(trijsturis1))


class BankAccount:
    def __init__(self, n, b):
        self.name = n
        self.balance = b

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise Exception("The withdrawal amount exceeds balance")

# account1 = BankAccount("Atis", 12)
# print(account1.name)
# print(account1.balance)
# account1.deposit(43)
# account1.withdraw(100)
# account1.deposit(10)
# print(account1.name)
# print(account1.balance)

# Klase Point2D, kas glabā divus atribūtus - x un y koordinātas. 
# Klases metodes moveUp(distance), moveRight(distance), moveDown(distance), moveLeft(distance), 
# kas attiecīgi pārvieto punktu koordinātu plaknē

# Papildināt klasi ar atribūtu totalTravelled, kas glabā un uzskaita kopējo pārvietojumu

class Point2D:
    def __init__(self, x, y):
        self.koord_x = x
        self.koord_y = y
        self.totalTravelled = 0

    def __str__(self):
        return f"Point at ({self.koord_x}; {self.koord_y})"

    def moveX(self, d):
        self.koord_x += d
        self.totalTravelled += abs(d)

    def moveY(self, d):
        self.koord_y += d
        self.totalTravelled += abs(d)

    def distanceTo(self, point):
        deltaX = abs(self.koord_x - point.koord_x)
        deltaY = abs(self.koord_y - point.koord_y)
        return (deltaX ** 2 + deltaY ** 2) ** 0.5
            
# p = Point2D(5, 8)
# o = Point2D(0, 1)
# v = Point2D(9, 3)
# print(o.distanceTo(v))
# print(Point2D.distanceTo(o, v))

# Implementējot Point2D klasi, realizēt programmu, kas ļauj ievadīt četras koordinātas. 
# Programma izveido četrus Point2D objektus un izmantojot 
# funkciju distanceTo() aprēķina ievadītās figūras perimetru un laukumu.

# For cikls, inputs, saraksti un pati Point2D klase

# For cikls garumā 4. Ievada koordinātas, 
# izmantojot koordinātas izveido Point2D objektus un saglabā sarakstā
count = 4
points = []
perimeter = 0

# for i in range(count):
#     x = int(input(f"ievadi {i + 1}. punkta x koordināti -> "))
#     y = int(input(f"ievadi {i + 1}. punkta y koordināti -> "))
#     points.append(Point2D(x, y))

# for i in range(count):
#     perimeter += points[i].distanceTo(points[(i + 1) % 4])

# print(perimeter)

# Klase Kvadratvienadojums, kas inicializācijas funkcijā saņem visus trīs koeficientus a, b un c.
# Klases iekšējās funkcijas realizē diskriminanta aprēķinu, sakņu aprēķinu, 
# parabolas virsotņu koordinātas un zaru virzienu (uz augšu/uz leju). 

# x2 - 4x + 5 = 0
# a = 1, b = -4, c = 5

class Kvadratvienadojums:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def __str__(self):
        return f"{self.a}x2 + {self.b}x + {self.c}" # <__main__.Kvadratvienadojums object at 0x0000027B5D66B770>

    def diskriminants(self):
        return self.b ** 2 - 4 * self.a * self.c
    
    def saknes(self):
        d = self.diskriminants()
        if d < 0:
            return []
        elif d == 0:
            return [-self.b/(2 * self.a)]
        else:
            x1 = (-self.b + d ** 0.5)/(2 * self.a)
            x2 = (-self.b - d ** 0.5)/(2 * self.a)
            return [x1, x2]
        
    def zariUzAugsu(self):
        return self.a > 0
    
    def virsotnesKoordinatas(self):
        x = -self.b / (2 * self.a)
        y = self.a * x ** 2 + self.b * x + self.c
        return [x, y]

u = Kvadratvienadojums(1, -4, 2)
print(u.virsotnesKoordinatas())
print(u.saknes())

# Klase Circle, kur ir divi iekšējie mainīgie - rādiuss un punkts, kas ir ar tipu Point2D
# Izveidot metodi/iekšējo funkciju isOverlapping(), kas nosaka, vai divi rinķi pārklājas

class Circle:
    def __init__(self, center: Point2D, radius: float):
        self.center = center
        self.radius = radius

    def isOverlapping(self, other):
        # ņemam attālumu starp centriem un salīdzinām ar abu rādiusu summu
        radiusSum = self.radius + other.radius
        distance = self.center.distanceTo(other.center)
        return radiusSum > distance
        
c1 = Circle(Point2D(1, 2), 4)
c2 = Circle(Point2D(1, 9), 2)
print(c1.isOverlapping(c2))