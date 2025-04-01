def funkcijasNosaukums(n):
    return 2 * n

p = funkcijasNosaukums(6)
print(p + 5)

# 50. Skaitlis par sarakstu. 673 -> [6, 7, 3]

def skaitlisParSarakstu(sk):
    saraksts = []
    while sk > 0:
        p = sk % 10
        sk = sk // 10
        saraksts.insert(0, p)
    return saraksts

# n = int(input("skaitlis: "))
# result = skaitlisParSarakstu(n)

# print(result)

# for num in result:
#     print("cipars", num)

# print(skaitlisParSarakstu(1425))
# print(skaitlisParSarakstu(74328))
# print(skaitlisParSarakstu(15))
# print(skaitlisParSarakstu(236))

# 52. Noņemt no saraksta _visus_ divniekus.

def nonemtVisusDivniekus(s):
    saraksts = s.copy()

    while saraksts.count(2) > 0:
        saraksts.remove(2)

    return saraksts

# 60. Dots saraksts s. Atrast tajā otro lielāko vērtību. Ņemt vērā duplikātus.

def otraLielaka(s):
    saraksts = s.copy()
    maximala = max(saraksts)

    while saraksts.count(maximala) > 0:
        saraksts.remove(maximala)

    return max(saraksts)

# 64. Atrast garāko vārdu tekstā.

def garakaisVards(text):
    words = text.split()
    garakais = words[0]

    for word in words:
        if len(word) > len(garakais):
            garakais = word

    return garakais

# 76. Dota simbolu virkne. Atrast tajā pirmo no 
#     simboliem, kas parādās vienu reizi jeb neatkārtojās.
#     "swijsuws" -> "i"

# def pirmaisKasNeatkartojas():
    
# 82. Funkcija, kas aprēķina saraksta modu. [1, 4, 6, 2, 1, 3] -> 1

def moda(s):
    if len(s) < 1:
        return None
    
    elif len(s) == 1:
        return s[0]
    
    biezhakais = s[0]
    for elem in s:
        if s.count(elem) > s.count(biezhakais):
            biezhakais = elem

    return biezhakais

# 83. Funkcija, kas saņem n un atgriež n-to Fibonači skaitli

# def fibonaci(n):
#     if n < 3:
#         return 1

#     x = 1 
#     y = 1
#     i = 3
#     while i < n:
#         z = x + y
#         x = y
#         y = z
#         i += 1

#     return x + y

# 84. Atzīmju kalkulators
#     ievade -> vidējā vērtība -> amplitūda -> biežākā vērtība

def inputAtzimes() -> list[int]:
    atzimes = []

    atz = int(input("atzīme: "))
    while atz > 0 and atz <= 10:
        atzimes.append(atz)
        atz = int(input("atzīme: "))

    return atzimes

def videjaAtzime(atzimes: list) -> float:
    return sum(atzimes) / len(atzimes)

def atzimjuAmplituda(atzimes: list) -> int:
    return max(atzimes) - min(atzimes)

def atzimjuModa(atzimes: list) -> int:
    if len(atzimes) < 1:
        return None
    
    elif len(atzimes) == 1:
        return atzimes[0]
    
    biezhakais = atzimes[0]
    for elem in atzimes:
        if atzimes.count(elem) > atzimes.count(biezhakais):
            biezhakais = elem

    return biezhakais

# atzimjuSaraksts = inputAtzimes()
# print(videjaAtzime(atzimjuSaraksts))
# print(atzimjuAmplituda(atzimjuSaraksts))
# print(atzimjuModa(atzimjuSaraksts))

# 85. Uzrakstīt četras funkcijas, katru ar atšķirīgu atgriežamās vērtības datu tipu.
#     list, integer, float/double, boolean, string

# visiSkaitlaDalitaji, skaitlaCipari saņem int, atgriež list
# tekstaFragments, genitivs saņem string, atgriež string

def isEven(num: int) -> bool:
    return num % 2 == 0

if isEven(2):
    print("yes")

# 86. Programma, kas saņem divas katetes un aprēķina hipotenūzu.

def hipotenuza(a:int, b:int) -> float:
    return (a ** 2 + b ** 2) ** 0.5

# 87. Programma, kas nosaka, vai skaitlis ir pirmskaitlis.

def isPrimeNumber(num:int) -> bool:
    dalitajuSkaits = 0
    for i in range(1, num + 1):
        if num % i == 0:
            dalitajuSkaits += 1

    return dalitajuSkaits == 2


if isPrimeNumber(int(input("Ievadi skaitli: "))):
    print("Jā")
else:
    print("Nē")



