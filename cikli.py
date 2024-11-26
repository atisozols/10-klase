# for <mainigais> in range(<intervals>):
# for _ in range(10): 
#     print("Hello world")

# viens parametrs iekš range(n) -> [0;n)
# for i in range(12):
#     print(i)

# divi parametri iekš range(n, m) -> [n;m)
# for i in range(1, 11):
#     print(f"šī ir {i}.reize")

# trīs parametri iekš range(n, m, k) -> [n; m) solis: k
# for i in range(5, 10, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# 19. Ievada n. Saskaitīt visus skaitļus no 1 līdz n ieskaitot.

# n = int(input("skaitlis n: "))
# summa = 0

# for i in range(1, n + 1):
#     summa = summa + i
#     print(f"i: {i}, summa: {summa}")

# print(summa)

# 20. Ievada piecus skaitļus un izvada to summu un vidējo vērtību.

# summa = 0
# n = 10

# for _ in range(n):
#     sk = int(input("skaitlis: "))
#     summa += sk # summa tiek palielināta par ievadīto sk

# print(summa)
# print(summa/n)

# 21. Izvadīt visus skaitļus no 1 līdz 100, kas dalās ar 3 vai 8.

# for i in range(1, 101):
#     if i % 8 == 0 or i % 3 == 0:
#         print(i)
        
# 22. Ievadīts n. Izvadīt pirmos n kvadrātus.
# 4 -> 1, 4, 9, 16

# n = int(input("n: "))
# for i in range(1, n + 1):
#    print(i ** 2)

# 23. Ievadīts n. Izvadīt visus kvadrātus, kas mazāki par n.
# Kvadrāts, kas mazāks par n -> skaitlis, kurš mazāks par kvadrātsakni no n

# n = int(input("n: "))
# n = round(n ** 0.5)
# for i in range(1, n + 1):
#    print(i ** 2)

# for i in range(1, n + 1):
#    if i ** 2 <= n:
#       print(i ** 2)
#    else:
#       break

# 24. Ievadīts skaitlis. Skaitlim nosakām dalītāju skaitu.

# n = int(input("n: "))
# skaits = 0

# for i in range(1, n + 1):
#    if n % i == 0:
#       skaits += 1

# print(skaits)

# 25. Ievadīts skaitlis. Noteikt, vai tas ir pirmskaitlis.

# n = int(input("n: "))

# for i in range(2, n):
#    if n % i:
#       print("nav pirmskaitlis")
#       break

# 26. Ievada n. Izvadīt pirmos n nepāra skaitļus.
# 5 -> 1, 3, 5, 7, 9

# n = int(input("n: "))
# for i in range(1, n * 2, 2):
#     print(i)

# sk = -1
# for _ in range(n):
#     sk += 2
#     print(sk)

# 27. Ievada n. Programma, kas izvada skaitļus no 1 līdz n vienā rindiņā.
# 1 2 3 4 ... n

# for i in range(1, int(input("n: ")) + 1):
#     print(i, end=" ")

# 28. Ievada n. Iegūt sekojošu izvadi:
# n: 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4  

# n = int(input("n: "))
# for i in range(n):
#     for i in range(1, n + 1):
#         print(i, end=" ")
#     print()

# 29. Ievada n. Iegūt sekojošu izvadi:
# n: 5
# 1 1 1 1 1
# 2 2 2 2 2 
# 3 3 3 3 3
# 4 4 4 4 4 
# 5 5 5 5 5

# n = int(input("n: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(i, end=" ")
#     print()


# 30. Ievada n. Iegūt sekojošu izvadi:
# n: 4
# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

# n = int(input("n: "))
# for i in range(1, n + 1):
#     for j in range(i, n + i):
#         print(j, end=" ")
#     print()

# 31. Ievada n. Iegūt sekojošu izvadi:
# n: 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# n = int(input("n: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# 32. Ievada n. Iegūt sekojošu izvadi:
# n: 4
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# skaitlis = 1
# n = int(input("n: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(skaitlis, end=" ")
#         skaitlis += 1
#     print()

# 33. Ievada n. Iegūt sekojošu izvadi:
# n: 5
# 1 1 1 1 1
# 1       1
# 1       1
# 1       1
# 1 1 1 1 1

# n = int(input("n: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or j == n - 1 or i == n - 1:
#             print(1, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 34. Ievada n. Izvadīt skaitļus 
# no n līdz 1 dilstošā secībā vienā rindiņā.

# for i in range(int(input("n: ")), 0, -1):
#     print(i, end=" ")

#### WHILE cikls

# n = 1
# while n < 11:
#     print(n)
#     n += 1

# 35. Vada skaitļus līdz tiek ievadīta 0.

# n = int(input("n: "))
# while n != 0:
#     n = int(input("n: "))

# 36. Vada skaitļus līdz tiek ievadīta 0. Izvadīt skaitļu summu. 

# summa = 0
# n = int(input("n: "))
# while n != 0:
#     summa += n
#     n = int(input("n: "))

# print(summa)

# 37. Patvaļīgi lielam skaitlim noteikt ciparu summu.

# sum = 0
# sk = int(input("skaitlis: "))
# while sk > 0:
#     p = sk % 10
#     sk = sk // 10
#     sum += p
# print(sum)
    
# 38. Patvaļīgi lielam skaitlim noteikt ciparu vid. aritm.

# sum = 0
# cip_sk = 0
# sk = int(input("skaitlis: "))
# while sk > 0:
#     p = sk % 10
#     sk = sk // 10
#     sum += p
#     cip_sk += 1
# print(sum/cip_sk)

# 39. Vada skaitļus līdz ievada 0. 
#     No visiem ievadītajiem noteikt lielāko.

# n = int(input("n: "))
# maksimalais = n
# while n != 0:
#     if n > maksimalais:
#         maksimalais = n
#     n = int(input("n: "))
# print(maksimalais)

# 40. Vada skaitļus līdz ievada 0. 
#     No visiem ievadītajiem noteikt mazāko.

# n = int(input("n: "))
# minimalais = n
# while n != 0:
#     if n < minimalais:
#         minimalais = n
#     n = int(input("n: "))
# print(minimalais)

# 41. Vada skaitļus līdz ievada 0. 
#     Noteikt skaitļu amplitūdu.

# n = int(input("n: "))
# maksimalais = n
# minimalais = n
# while n != 0:
#     if n > maksimalais:
#         maksimalais = n
#     if n < minimalais:
#         minimalais = n
#     n = int(input("n: "))

# print(maksimalais - minimalais)

# 42. Vada skaitļus līdz ievada 0. 
#     Sākot no otrā ievadītā, noteikt tā
#     attiecību pret iepriekš ievadīto.
# n: 3
# n: 5
# 5 ir lielāks par 3
# n: 2
# 2 ir mazāks par 5
# n: 

# n = int(input("skaitlis: "))
# m = int(input("skaitlis: "))

# while m != 0:
#     if n != m:
#         print(f"{max(n, m)} ir lielāks nekā {min(n, m)}")
#     else:
#         print("vienādi")
#     n = m
#     m = int(input("skaitlis: "))

# 43. Vada skaitļus līdz ievada 0. Noteikt, vai tika
#     ievadīti vairāk pāra vai nepāra skaitļi. (35.)

# ind = 0

# n = int(input("n: "))
# while n != 0:
#     if n % 2 == 0:
#         ind += 1
#     else:
#         ind -= 1
#     n = int(input("n: "))

# if ind > 0:
#     print("pāra ir vairāk")
# elif ind < 0:
#     print("nepāra ir vairāk")
# else:
#     print("vienādi")

# 44.1 Patvaļīgi lielu skaitli izvadīt pretējā secībā. (37.)
#      4761 -> 1674
# 44.2 Noteikt, vai ievadītais skaitlis ir simetrisks.
#      387 -> nav
#      10001 -> ir

# num = int(input("sk: "))
# old_sk = num
# new_sk = 0

# while num > 0:
#     p = num % 10
#     new_sk = new_sk * 10 + p
#     num = num // 10

# if new_sk == old_sk:
#     print("simetrisks")
# else:
#     print("asimetrisks")


# Nejaušība
# import random
# n = random.randint(1, 10)

# 45.1 Vada skaitļus līdz tiek uzminēts uzģenerētais skaitlis.

# minejums = int(input("minējums: "))
# while n != minejums:
#     minejums = int(input("minējums: "))

# print("Pareizi")

# 45.2 Tiek parādīts minējumu skaits, kad uzmin.

# import random
# n = random.randint(1, 10)

# minejumuSkaits = 1
# minejums = int(input("minējums: "))
# while n != minejums:
#     minejumuSkaits += 1
#     minejums = int(input("minējums: "))

# print(f"Pareizi, uzminēji ar {minejumuSkaits} minējumiem")

# 45.3 Programma palīdz minēt, pasakot priekšā, vai vēlamais
#      ir lielāks vai mazāks nekā minējums. 

# import random
# n = random.randint(1, 1000)

# minejums = int(input("minējums: "))
# minejumuSkaits = 1
# while n != minejums:
#     if n > minejums:
#         print("lielāks")
#     else:
#         print("mazāks")
#     minejums = int(input("minējums: "))
#     minejumuSkaits += 1

# print("Pareizi")

# 46. Akmens-šķēres-papīrīts

# import random

# W_LIMIT = 3
# comp_w = 0
# user_w = 0

# while comp_w < W_LIMIT and user_w < W_LIMIT:
#     comp = random.randint(1, 3)
#     user = int(input("akmens: 1\nšķēres: 2\npapīrs: 3\ntavs gājiens: "))

#     if user == comp:
#         print("neizšķirts")
#     elif (user == 1 and comp == 2) or (user == 2 and comp == 3) or (user == 3 and comp == 1):
#         print("uzvara")
#         user_w += 1
#     else:
#         print("zaudējums")
#         comp_w += 1
#     print(f"rezultāts {user_w}:{comp_w}")   

# if comp_w > user_w:
#     print("dators uzvarēja")
# else:
#     print("tu uzvarēji")

# 46.1 Streak

# 47. Karsts-auksts minēšana

# 48. Programma, kas ģenerē matemātikas uzdevumus:
#     1) 10 uzdevumi saskaitīšanā/atņemšanā
#     2.1) Lietotājs netiek uz priekšu, kamēr nav pareiza atbilde
#     2.2) Lietotājs iet uz priekšu neatkarīgi vai pareizs. Beigās parāda atzīmi.

# 10 + 5 =
# 12
# 10 + 5 =
# 15
# 9 - 2 = 
# 7
#  

# import random

# atz = 0
# for _ in range(10):
#     x = random.randint(1, 10)
#     y = random.randint(1, 10)
#     darbiba = random.choice([1, -1])
#     result = x + y * darbiba

#     guess = int(input(f"{x} {'+' if darbiba > 0 else '-'} {y} = "))
#     # if guess == result:
#     #     atz += 1
#     while result != guess:
#         guess = int(input(f"{x} {'+' if darbiba > 0 else '-'} {y} = "))

# print(f"atzime: {atz}")

# break a loop

# dalSk = 0
# n = int(input("n: "))
# for i in range(2, n):
#     if n % i == 0:
#         dalSk += 1
#         break

# if dalSk > 0:
#     print("nav pirmskaitlis")
# else:
#     print("pirmskaitlis")
