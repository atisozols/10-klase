# print("šis netiek palaists")

# print("Hello")
# nameCopy = "Atis"
# name = input("ievadi vārdu: ")
# print("Tavs vārds ir: ", name, 5.5)
# print(f"Tavs vārds ir {name}")

# skolenaVecums = 16 # camelCase
# skolena_vecums = 16 # snake_case

# Matemātiskas darbības
# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)


# Sazarojumi

# x = int(input("ievadi skaitli x: "))

# if x > 5:
#     print("x ir lielāks par 5")
# else:
#     if x == 5:
#         print("x ir vienāds ar 5")
#     else:
#         print("x ir mazāks par 5")


# if x > 5:
#     print("x ir lielāks par 5")
# elif x == 5:
#     print("x ir vienāds ar 5")
# else:
#     print("x ir mazāks par 5")

# 1. Ievada skaitli. Programma nosaka, vai tas 
#    ir lielāks par nulli, mazāks vai vienāds.

# x = int(input("ievadi x: "))

# if x > 0:
#     print("x ir lielāks par 0")
# elif x == 0:
#     print("x ir vienāds ar 0")
# else:
#     print("x ir mazāks par 0")

# 2. Ievada dienas numuru (1-7). Programma nosaka, vai tā 
#    ir darba diena vai brīvdiena. Tad nosakām dienas nosaukumu.

# diena = int(input("ievadi dienu: "))

# if diena > 5:
#     print("brīvdiena")
# else:
#     print("darba diena")

# if diena == 1:
#     print("pirmdiena")
# elif diena == 2:
#     print("otrdiena")
# elif diena == 3:
#     print("trešdiena")
# elif diena == 4:
#     print("ceturtdiena")
# elif diena == 5:
#     print("piektdiena")
# elif diena == 6:
#     print("sestdiena")
# elif diena == 7:
#     print("svētdiena")
# else:
#     print("nepareiza ievade")

# 3. Ievadīti 3 skaitļi - a, b un c. Programma nosaka, vai 
#    ar šiem skaitļiem var izveidot trijstūri.

# a = int(input("ievadi a: ")) 
# b = int(input("ievadi b: ")) 
# c = int(input("ievadi c: ")) 

# # 1. variants
# if a + b > c:
#     if a + c > b:
#         if b + c > a:
#             print("ir trijstūris")
#         else:
#             print("nav")
#     else:
#         print("nav")
# else:
#     print("nav")

# # 2. variants
# if a + b > c and a + c > b and b + c > a:
#     print("ir trijstūris")
# else:
#     print("nav trijstūris")

# # 3. variants
# skaititajs = 0
# if a + b > c:
#     skaititajs = skaititajs + 1
# if a + c > b:
#     skaititajs = skaititajs + 1
# if b + c > a:
#     skaititajs = skaititajs + 1

# if skaititajs > 2:
#     print("ir trijstūris")
# else:
#     print("nav trijstūris")

# 4. Ievada trīs skaitļus. Programma no tiem nosaka lielāko.
  
# a = int(input("ievadi a: ")) 
# b = int(input("ievadi b: ")) 
# c = int(input("ievadi c: ")) 

# if a >= b and a >= c:
#     print(a)
# elif c >= b and c >= a:
#     print(c)
# else:
#     print(b)

# temperatura = 18
# irSilts = temperatura > 15

# print(irSilts)

# 5. Ievadīti trīs mainīgie a, b, c. 
#    Atrisināt un izvadīt saknes kvadrātvienādojumam 
#    ar šiem koeficientiem.

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# diskriminants = b ** 2 - 4 * a * c

# if diskriminants < 0:
#     print("sakņu nav")
# elif diskriminants == 0:
#     x = -b/(2 * a)
#     print(f"viena sakne: {x}")
# else:
#     x1 = (-b + diskriminants ** 0.5)/(2 * a)
#     x2 = (-b - diskriminants ** 0.5)/(2 * a)
#     print(f"x1 = {x1}, x2 = {x2}")

# xVirsotne = x = -b/(2 * a)
# yVirsotne = (a * xVirsotne ** 2) + (b * xVirsotne) + c

# print(f"virsotne atrodas punktā ({xVirsotne}, {yVirsotne})")
# print("virsotne atrodas punktā (", xVirsotne, ", ", yVirsotne, ")")

# 6. Ievadīts skaitlis. Noteikt, vai tas ir pāra.

# x = int(input("ievadi skaitli: "))

# if x % 2 == 0:
#     print("dalās")
# else:
#     print("nedalās")

# 7. Ievadīts divciparu skaitlis. Aprēķināt šim skaitlim ciparu summu.

# x = 563
# cipars2 = x % 10 # 3
# cipars1 = x // 100 # 5
# print(cipars1 + cipars2)

# 8. Programma pieprasa ievadīt divus skaitļus. 
#    8.1. Izvada, kurš no skaitļiem ir lielāks.
#    8.2. Izvada pāra skaitli. Ja abi ir pāra, izvada abus.
#         Ja neviens nav pāra, neizvada neko.

# a = int(input("ievadi skaitli: "))
# b = int(input("ievadi skaitli: "))

# if a > b:
#     print("a ir lielāks")
# else:
#     print("b ir lielāks")

# if a % 2 == 0:
#     print(a)

# if b % 2 == 0:
#     print(b)

# 9. Lietotājs ievada dienu gadā (1-365). Programma izvada, vai 
#    tā ir darba diena vai brīvdiena. Pieņem, ka pirmais janvāris ir pirmdiena.

# dienasNr = int(input("dienas nr: "))

# if dienasNr % 7 == 0 or dienasNr % 7 == 6:
#     print("brīvdiena")
# else:
#     print("darba diena")

# 10. Vērdiņā stāv bezgalīgi daudz 10EUR un 5EUR banknotes, 2EUR monētas un 1EUR monētas.
#     Tiek ievadīts skaitlis - summa, kas jāsamaksā. Izveidot programmu, kas nosaka, 
#     kā šo summu samaksāt ar pēc iespējas mazāk naudas vienībām.

summa = int(input("summa: "))

# cik nomināli ieiet summā, ar cik desmitniekiem es varu šo samaksāt
print(f"sākuma summa: {summa}")
desmitniekuSkaits = summa // 10
# noņemu no summas desmitnieku skaitu sareizinātu ar to vērtību (piemēram, 4 banknotes ir 4*10=40EUR)
summa = summa - desmitniekuSkaits * 10 # cik paliek pāri, kad iztērējam desmitniekus
print(f"iztērēju {desmitniekuSkaits} desmitniekus un pāri palika: {summa}")

piecisuSkaits = summa // 5
summa = summa - piecisuSkaits * 5
print(f"iztērēju {piecisuSkaits} pieciniekus un pāri palika: {summa}")

divniekuSkaits = summa // 2
summa = summa - divniekuSkaits * 2
print(f"iztērēju {divniekuSkaits} divniekus un pāri palika: {summa}")

print(f"šo var samaksāt ar {desmitniekuSkaits} desmitniekiem, {piecisuSkaits} piecīšiem, {divniekuSkaits} divīšiem un {summa} vienīšiem")


# 11. Ievada divus skaitļus - dienu un mēnesi. Programma nosaka rītdienas datumu.



# 2, 12 -> 3, 12
# 28, 2 -> 1, 3
# 30, 9 -> 1, 10
# 31, 12 -> 1, 1

# 1) pārbaudām, kurš mēnesis, lai zinātu, kur ir mēneša beigas
# 2) pārbaudām, vai ir mēneša beigas
# 3) palielinām dienu par 1 VAI palielinām mēnesi un dienu nomainam uz 1

# 2 -> 28
# 4, 6, 9, 11 -> 30
# visi pārējie -> 31

# ievadām divas vērtības
day, month = int(input("diena: ")), int(input("mēnesis: "))

# saglabāju kopiju, lai rezultātā varu 
# parādīt gan pašreizējo, gan jauno aprēķinu
yesterday, yestermonth = day, month

# sākumā paskatāmies uz mēnesi, 
# jo nezinot mēnesi, nezināsim, vai ir mēneša beigas
if month == 2:
    # zinot mēnesi, varam attiecīgi pārbaudīt, vai ir mēneša pēdējā diena
    if day == 28:
        day = 1
        month = month + 1
    else:
        # ja nav mēneša pēdējā diena, palielinam tikai dienu, piemēram 15/3 -> 16/3
        day += 1

elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        day = 1
        month += 1 # month = month + 1
    else:
        day += 1

else:
    if day == 31:
        day = 1

        # ja šis ir 1., 3. utt mēnesis, tad atlikuma operators neko nemaina
        # vienīgā situācija ir (12+1)%12
        month = (month + 1) % 12
    else:
        day += 1

print(f"šodien ir {yesterday}/{yestermonth}")
print(f"rītdien ir {day}/{month}")

# 12. Dots dienas numurs gadā. 
#     Noteikt, vai tā ir pāra vai nepāra nedēļa.
#     Pieņemt, ka pirmā diena ir pirmdiena.
#     5 -> nepāra
#     40 -> nepāra

# 1.-7. diena ir 1. nedēļa
# 8.-14. diena ir 2. ned.
# utt.

# ievadām dienu, atņemot 1, pabīdām intervālu uz atpakaļu (1-7) -> (0-6)
day = int(input("diena: ")) - 1 
# (0-6) // 7 -> 0
# (7-13) // -> 1

# aprēķinām nedēļas numuru, pieskaitot 1 numurs tiek pārveidots par _pozitīvu_
nedelasNr = day // 7 + 1

# pāra skaitļiem dalījums ar 2 atlikumā dod 0
if nedelasNr % 2 == 0:
    print("pāra nedēļa")
else:
    print("nepāra nedēļa")


# 13. Bolt Drive maksā gan minūtē, gan kilometros. 
#     Pie cenas 0.13/min un 0.29/km aprēķināt aptuveno 
#     kilometra cenu pilsētā, ja vidējais kustības ātrums ir 40km/h
#     Ievada kilometrus, izvada cenu.

# distance = int(input("km: "))
# kmCena = 0.29 * distance
# laikaCena = distance / 40 * 60 * 0.13
# print(kmCena + laikaCena)

# 14. Izstrādāt programmu, kurai ir vismaz 6 dažādi iznākumi. 
#     Simulēt lēmumu pieņemšanu, ko veicat. 
#     Piemērs: 
#     Ievada laikapstākļus (temp un nokrišņus), programma iedod vēlamo apģērbu.
#     VAI Piemērs: 
#     Ievada dienas daļu, ēdiena vēlmes un programma iedot piemērotāko maltīti

# age = int(input("vecums: "))

# if age < 13:
#     print("bērniem bezmaksas ieeja")
# elif age < 18:
#     statuss = input("skolēns? jā/nē ")
#     if statuss == "jā":
#         print("skolēna cena 3EUR")
#     else:
#         print("jauniešu cena 5EUR")
# elif age < 65: 
#     statuss = input("students? jā/nē ")
#     if statuss == "jā":
#         print("studenta cena 5EUR")
#     else:
#         print("pieaugušo cena 8EUR")
# else:
#     print("pensionāru cena 3EUR")

# 15. Ievadīti divi cipari. Izveidot no tiem pāra skaitli, 
#     ja tas ir iespējams. Ja nav, tad izveidojam pāra
#     skaitli, saskaitot ciparus.
#     4, 5 -> 54
#     7, 6 -> 76
#     2, 0 -> 20 vai 2
# #     7, 5 -> 12

x, y = int(input("pirmais:")), int(input("otrais:"))

if y % 2 == 0:
    print(f"{x}{y}")
elif x % 2 == 0:
    print(f"{y}{x}")
else:
    print(x + y)
    
