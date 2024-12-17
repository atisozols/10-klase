#      0  1  2  3  4  5  6  7
# s = [1, 3, 7, 2, 8, 2, 7, 2]

# print(s[4])
# print(s[-2])
# print(s[2:6])
# print(s[2:])
# print(s[:6])

# s.append(11)
# s.insert(2, 6)

# s[2] = 6

# s.pop()
# s.pop(0)
# s.remove(7)

# print(len(s))
# print(s.count(2))

# print(s)

# s = [1, 3, 7, 2, 8, 2, 7, 2]
# t = [9, 1, 3]
# v = s + t # [1, 3, 7, 2, 8, 2, 7, 2, 9, 1, 3]
# print(v)

# print(len(s))
# print(sum(s))
# print(min(s))
# print(max(s))

# 49. Dots saraksts. Izvadīt pāra elementus.

#    0  1  2  3  4  5  6  7
# s = [1, 3, 7, 2, 8, 2, 7, 2]

# for i in range(8): [0; 8)
# for i in range(len(s)):
#     if s[i] % 2 == 0:
#         print(s[i])

# for el in s:
#     if el % 2 == 0:
#         print(el)

# s = []

# n = int(input("n: "))
# while n != 0:
#     s.append(n)
#     n = int(input("n: "))

# print(s)


# 50. Skaitlis par sarakstu. 673 -> [6, 7, 3]

# saraksts = []
# sk = int(input("skaitlis: "))
# while sk > 0:
#     p = sk % 10
#     sk = sk // 10
#     saraksts.insert(0, p)

# print(saraksts)

# 51. Saraksts par skaitli. [2, 8, 4] -> 284


#        0 | 6 | 61 | 612 | 6123 | 61234
# result = 0 
# cipari = [6, 1, 2, 3, 4]

# for cipars in cipari:
#     result *= 10
#     result += cipars

# print(result)

# s = [1, 3, 7, 2, 8, 2, 7, 2]

# 52. Noņemt no saraksta _visus_ divniekus.

# divniekuSkaits = s.count(2)

# for _ in range(divniekuSkaits):
#     s.remove(2)

# while s.count(2) > 0:
#     s.remove(2)

# print(s)

# 53. Atrast sarakstā biežāk sastopamo elementu.
# s = [1, 3, 7, 7, 2, 8, 2, 7, 2]

# kandidats = s[0]
# kandidataSkaits = s.count(s[0])

# for element in s:
#     if s.count(element) > kandidataSkaits:
#         kandidats = element
#         kandidataSkaits = s.count(element)

# print(kandidats)

# kārtošana

# s = [1, 3, 7, 7, 2, 8, 2, 7, 2]
# s.sort()
# s.sort(reverse=True)
# print(s)

# 54. Vada skaitļus, kamēr ievada nulli. 
#     No skaitļiem izveido sarakstu. Atrast sarakstā mediānu.

# s = []

# n = int(input("n: "))
# while n != 0:
#     s.append(n)
#     n = int(input("n: "))

# s.sort()

# print(s)

# if len(s) % 2 == 0: # ja saraksta ir pāra skaits elementi
#     i1 = len(s) // 2
#     i2 = len(s) // 2 - 1
     
#     print((s[i1] + s[i2]) / 2)
# else:
#     i = len(s) // 2

#     print(s[i])

# 55. Dots saraksts. Izmantojot while, izvadīt visus elementus.

# s = [1, 3, 7, 7, 2, 8, 2, 7, 2]

# i = 0

# while i < len(s):
#     print(s[i])
#     i += 1

# 56. Dots saraksts. Izmantojot while, izvadīt visus elementus no otra saraksta gala.

# s = [1, 3, 7, 7, 2, 8, 2, 7, 2]

# i = len(s) - 1

# while i >= 0:
#     print(s[i])
#     i -= 1

# 57. Dots saraksts. Lietotājs ievada n. Noteikt vismaz 
#     vienu skaitļu pāri no saraksta, kas summā veido n.

# s = [1, 3, 7, 7, 2, 8, 8, 2, 7, 2]

# s.sort()
# print(s[-2])

# n = int(input("n: "))

# for i in range(len(s)):
#     for j in range(i, len(s)):
#         # print(f"s[i] = {s[i]} i = {i} s[j] = {s[j]} j = {j}")
#         if s[i] + s[j] == n and i != j:
#             print(i, j)

# 58. Dots saraksts s. Izveidot jaunu sarakstu, kas satur s vērtības apgrieztā kārtībā.

# s = [1, 3, 7, 7, 2, 8, 2, 7, 2]
# s_copy = []

# i = len(s) - 1

# while i >= 0:
#     s_copy.append(s[i])
#     i -= 1

# print(s)
# print(s_copy)

# 59. Dots saraksts s. Izvadīt no saraksta tos elementus, kas tajā parādās tikai vienu reizi.
# #    0  1  2  .. 
# s = [1, 3, 7, 7, 2, 8, 2, 7, 2]

# for elem in s:
#     if s.count(elem) == 1:
#         print(elem)

# for i in range(len(s)):
#     if s.count(s[i]) == 1:
#         print(s[i])

# 60. Dots saraksts s. Atrast tajā otro lielāko vērtību. Ņemt vērā duplikātus.

# s = [1, 3, 7, 7, 2, 8, 2, 7, 2, 8]

# l = max(s)

# while s.count(l) > 0: # while l in s:
#     s.remove(l)

# print(max(s))

# s.sort(reverse=True)

# i = 0

# while s[i] == max(s):
#     i += 1

# print(s[i])

# 61. Dots saraksts s. Lietotājs ievada n. Izveidot jaunu sarakstu, pagriežot s pa n pozīcijām.
# Piemērs: s = [1, 2, 3, 4, 5]; n = 2; result = [4, 5, 1, 2, 3] 

# #    0  1  2  3  4  5  6
# s = [1, 2, 3, 4, 5, 6, 7]


# for n in range(len(s)):
#     print(s[-n:] + s[:-n])

