class Taisnsturis:
    def __init__(self, x, y):
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
        return f"Point at ({self.koord_x}; {self.koord_y}). Total distance: {self.totalTravelled}"

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
            
p = Point2D(5, 8)
o = Point2D(0, 1)
v = Point2D(9, 3)
print(o.distanceTo(v))
print(Point2D.distanceTo(o, v))

# Implementējot Point2D klasi, realizēt programmu, kas ļauj ievadīt četras koordinātas. 
# Programma izveido četrus Point2D objektus un izmantojot 
# funkciju distanceTo() aprēķina ievadītās figūras perimetru un laukumu.
