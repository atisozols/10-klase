# name = "estere"

# for char in name:
#     print(char)

# for i in range(len(name)):
#     if name[i] == 'e':
#         print(name[i])

# print(name.count('t'))

# print(name.replace("estere", "atis"))

# name[2] = 'x' nav iespējams

# name2 = ''

# for i in range(len(name)):
#     if i != 2:
#         name2 += name[i]
#     else: 
#         name2 += 'x'

# print(name2)

# text = "kā tevi sauc?"

# print(text.split())

# 62. Lietotājs ievada tekstu. Izvadīt vārdu skaitu tekstā.



# print(len(text.split()))
# print(text.count(" ") + 1)

# 63. Izvadīt tekstu, apgriežot katru vārdu, taču paturot vārdu secību.
# text = input("ievadi tekstu: ")
# words = text.split()

# for w in words:
#     for i in range(len(w) - 1, -1, -1):
#         print(w[i], end="")
#     print()

# 64. Atrast garāko vārdu tekstā.

# text = input("ievadi tekstu: ")
# words = text.split()

# garakais = words[0]

# for w in words:
#     if len(w) > len(garakais):
#         garakais = w

# print(garakais)

# 65. Izņemt visas atstarpes tekstā.

# text = input("ievadi tekstu: ")

# words = text.split()

# for w in words:
#     print(w, end="")

# 66. Neņemot vērā atstarpes, noteikt, vai teksts ir palindroms.
#     alusari ira sula -> ir

# text = input("ievadi tekstu: ")

# words = text.split()

# t = ""
# for w in words:
#     t += w

# t_reversed = ""
# for i in range(len(t) - 1, -1, -1):
#     t_reversed += t[i]

# print(t, t_reversed)
# if t == t_reversed:
#     print("ir palindroms")
# else:
#     print("nav")

# 67. Dota simbolu virkne ar 0 un 1. Atrast garāko distanci starp nullēm.
#     ---->
# sv = "111111111100111001111110001110111111111" # atbilde: 6

# maxVieniniekuSkaits = 0
# vieniniekuSkaits = 0
# irBijusiNulle = False # Ja, šis ir 0, tas nozīmē, ka vēl nav bijusi neviena nulle

# for char in sv:
#     if char == "0":
#         irBijusiNulle = True
#         if vieniniekuSkaits > maxVieniniekuSkaits:
#             maxVieniniekuSkaits = vieniniekuSkaits
#             vieniniekuSkaits = 0
#     else:
#         if irBijusiNulle:
#             vieniniekuSkaits += 1
            
# print(maxVieniniekuSkaits)

# 68. Ievadīts teksts. Noteikt, vai tas ir pareizi uzrakstīts e-pasts.

# email = "atis@mail.com"

# atSimbols = False
# valid = False

# for char in email:
#     if char == "@":
#         atSimbols = True
#     elif char == "." and atSimbols:
#         valid = True
#         break

# if valid:
#     print("ir pareizs")
# else:
#     print("nav pareizs")

# 69. Dots teksts ar iekavām. Noteikt, vai iekavas lietotas pareizi.
#     Piemērs: "(())()" -> pareizi
#              ")((()" -> nepareizi
#              ")))(((" -> nepareizi

# text = "(2 + 4 * (1 - 5)) + 2 + (5^2)"
# stavoklis = 0
# valid = False

# for char in text:
#     if char == "(":
#         stavoklis += 1
#     elif char == ")":
#         stavoklis -= 1

#     if stavoklis < 0:
#         valid = False
#         break

# if stavoklis == 0:
#     valid = True

# if valid:
#     print("ir pareizs")
# else:
#     print("nav pareizs")

# 70. Dota izteiksme ar iekavām. Izvadīt to tekstu, kas nav iekļauts iekavās.
# "abc(de(fg)hij)kl(mn)op" -> abcklop

# text = "abc(de(fg)hij)kl(mn)op"
# stavoklis = 0
# valid = False
# t = ""

# for char in text:
#     if char == "(":
#         stavoklis += 1
#     elif char == ")":
#         stavoklis -= 1
#     elif stavoklis == 0:
#         t += char

#     if stavoklis < 0:
#         valid = False
#         break

# print(t)  

# if stavoklis == 0:
#     valid = True

# if valid:
#     print("ir pareizs")
# else:
#     print("nav pareizs")

## Piemērs

# char = "Atis"
# pārvērš tekstu
# print(char.capitalize())
# print(char.upper())
# print(char.lower())

# pārbauda tekstu
# print(char.islower())
# print(char.isupper())
# print(char.istitle())

# 71. Dots teksts. Katru vārdu sākt ar lielo burtu.

# text = "tukUMa raIna valSts giMNazIja"

# for word in text.split():
#     print(word.capitalize(), end=" ")

# 72. Dots teksts. Noteikt, cik vārdi tekstā sākas ar lielo burtu.

# text = "Tukuma Raina Valsts gimnazija"
# sum = 0
# for word in text.split():
#     if word.istitle():
#         sum += 1
# print(sum)
