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

# 68. Ievadīts teksts. Noteikt, vai tas ir pareizi uzrakstīts e-pasts. ___@___.__

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
# # pārvērš tekstu
# print(char.capitalize())
# print(char.upper())
# print(char.lower())

# # pārbauda tekstu
# print(char.islower())
# print(char.isupper())
# print(char.istitle())
# print(char.isalpha())

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

# 73. Ievadīts teksts. Tekstā atrast tos vārdus, kas beidzas ar burtu "t".

# text = "darīt vai nedarīt - tāds ir jautājums" # darīt; nedarīt

# 74. Ievadīts teksts. Noteikt, vai tekstā sastopami visi patskaņi.

# text = ""
# patskani = "aeiou"

# word = "atis"

# for p in patskani:
#     if p in word:
#         print(1)

# 75. Ievadīts teksts/simbolu virkne. Atdalīt neburtu 
#     simbolus no burtiem un izvadīt tos atsevišķi.
#     "abc123de45f6" -> "abcdef" un "123456"

# 76. Dota simbolu virkne. Atrast tajā pirmo no 
#     simboliem, kas parādās vienu reizi jeb neatkārtojās.
#     "swijsuws" -> "i"

# IESIEGŠANA - https://github.com/atisozols/10-klase/blob/main/simbolu_virknes/simbVirknes_fv.md

# 78. Dots teksts/simbolu virkne un skaitlis n. Norotēt simbolu virkni pa n simboliem.
#     peteris, 2 -> terispe
#     peteris -> eterisp -> terispe -> erispet -> ..

# text = "peteris"
# n = 2

# print(text[n:] + text[:n])

# 79. Divas simbolu virknes. Noteikt, vai rotējot vienu ir iegūstama otra.
#     terispe, peteris -> jā
#     atis, sita -> nē

# w1 = "tukums"
# w2 = "kumstu"
# found = False

# for n in range(len(w1)):
#     if w2 == w1[n:] + w1[:n]:
#         found = True
#         break

# print("jā" if found else "nē")

# if found:
#     print("jā")
# else:
#     print("nē")

# 80. Ievadīts teksts/simb. virkne. Programma nosaka, vai no tekstā 
#     esošajiem simboliem iespējams izveidot palindromu.
#     nana -> ir
#     nanan -> ir -> annna
#     abcdd -> nav

# potential_palindrome = "aaaaaaa"  # aannnaa

# not_repeating_chars = ""

# even = 0
# uneven = 0

# for char in potential_palindrome: 
#     if not char in not_repeating_chars:
#         not_repeating_chars += char

# for char in not_repeating_chars:
#     if potential_palindrome.count(char) % 2 == 0:
#         even += 1
#     else:
#         uneven -= 1

# if uneven <= 1:
#     print("jā")
# else:
#     print("nē")

# 81. Dota izteiksme ar iekavām. Izvadīt to tekstu, kas atrodas visdziļāk iekavās.
# "abc(de(fg)hij)kl(mn)op" -> fg

text = "abc(de(fg)hij)kl(mn)op"
stavoklis = 0
max_stavoklis = 0
valid = False
t = ""

for char in text:
    if char == "(":
        stavoklis += 1
    elif char == ")":
        stavoklis -= 1
    elif stavoklis > max_stavoklis:
        t = ""
        max_stavoklis = stavoklis
        t += char
    elif stavoklis == max_stavoklis:
        t += char

    if stavoklis < 0:
        valid = False
        break

print(t)

if stavoklis == 0:
    valid = True

if valid:
    print("ir pareizs")
else:
    print("nav pareizs")
