# 5. uzd

# text = "sansusi"
# target = "s"
# count = 0

# for char in text:
#     if target == char:
#         count += 1

# print(count)

# 6. uzdevums

# full_name = input("ievadi vārdu un uzvārdu: ") #    Atis    Ozols
# words = full_name.split() # ['Atis', 'Ozols']
# first_name = words[0]
# last_name = words[1]

# print(f"{last_name}, {first_name}")
# print(last_name, ",", first_name)

# 7. uzdevums

# answer = input("Do you agree? (yes/no): ")

# answer = answer.strip().upper()

# if answer == "YES":
#     print("Accepted")
# else:
#     print("Rejected")

# 8. uzdevums

# word = "bad"
# text = input("Write a comment: ")
# text = text.replace(word, "***")
# print(text)

# 9. uzdevums

# text = input("ievadi teikumu: ")
# words = text.split()
# print(len(words))
# print(words[0])
# max_garums = 0
# max_vards = ""
# for word in words:
#     if len(word) > max_garums:
#         max_garums = len(word)
#         max_vards = word
#     print(word, max_vards)

# haystack = "tukuma raina valsts gimnazijas valsts skoleni"
# needle = "valsts"

# if haystack.find(needle) == -1:
#     print("nav tekstā")
# elif haystack.find(needle) == haystack.rfind(needle):
#     print(haystack.find(needle))
#     print(haystack.rfind(needle))
# else:
#     print(haystack.find(needle))
#     print(haystack.rfind(needle))
#     f = haystack.find(needle) + len(needle)
#     l = haystack.rfind(needle)
#     print(haystack[f:l]) # text[sakums:beigas-neieskaitot]


# teikums = input("Ievadiet teikumu: ")

# teikums_saraksts = teikums.split() # ['drīz', 'beigsies', 'nodarbība', 'šodien']

# print(len(teikums_saraksts)) 
# print(teikums_saraksts[0])

# text = "tukuma raina valsts gimnazija"
# words = text.split()
# result = ""
# for word in words:
#     result += word[0].upper()
# print(result)

# garakaisVards = ""
# for vards in teikums_saraksts:
#     if len(vards) > len(garakaisVards):
#         garakaisVards = vards

# print(garakaisVards)

# product = input("Product name: ")
# price = float(input("Price: "))
# qty = int(input("Quantity: ")) 
 
# print(f"{qty}gab. {product} (cena par vienību: {price}) Kopā: {round(qty * price, 2)}")

# # 11. uzd.

# text = input("Enter text: ") # šodien viss būs ok un rīt arī viss būs ok
# keyword = input("Enter keyword: ") # viss

# pirmoReizParadas = text.find(keyword) # 7
# pedejoReizParadas = text.rfind(keyword) # 30

# if pirmoReizParadas != pedejoReizParadas:
#     print(text[pirmoReizParadas + len(keyword):pedejoReizParadas]) # text[sakums:beigasNeieskaitot]

# #  un rīt arī viss būs 

# 12. uzd.

# parole = input("parole: ")

# atstarpjuSkaits = 0
# lieloBurtuSkaits = 0
# ciparuSkaits = 0

# for simbols in parole:
#     if simbols == " ":
#         atstarpjuSkaits += 1

#     if simbols.isupper():
#         lieloBurtuSkaits += 1

#     if simbols.isdigit():
#         ciparuSkaits += 1

# if len(parole) > 7 and atstarpjuSkaits == 0 and lieloBurtuSkaits > 0 and ciparuSkaits > 0:
#     print("Strong")
# else:
#     print("Weak")

# text = input("ievadi tekstu: ").strip()
# varduSaraksts = text.split()
# akronims = ""

# for vards in varduSaraksts:
#     akronims += vards[0]

# akronims = akronims.upper()

# 1) Vienkāršākais (un ļoti saprotams): pārbaudi visus fragmenta garumus
# n = len(s)
# Ej cauri iespējamajiem fragmenta garumiem L no 1 līdz n//2
# Fragmenta garumam jādalās: n % L == 0
# f = s[:L]
# Pārbaudi: f * (n // L) == s
# Pirmais L, kas strādā, ir īsākais fragments. Tad drukā:
# YES un f
# Ja neviens neder, drukā NO.

s = "ababab"
# reizinajums = ""
# print(s)

# for i in range(1, len(s) // 2 + 1):
#     if len(s) % i == 0:
#         reizinajums = s[:i] * (len(s) // len(s[:i]))
#         if s == reizinajums:
#             print("YES", s[:i])
#             break
#         else:
#             reizinajums = ""

# if len(reizinajums) == 0:
#     print("NO")


# s = "abcba"

# i = 0
# j = len(s) - 1
# valid = True
    
# while i <= j:
#     if s[i] != s[j]:
#         valid = False
#         break
#     i += 1
#     j -= 1

# if valid:
#     print("Ir palindroms")
# else:
#     print("Nav palindroms")


# 16. 

# s = "11101100111111011111111011"
# max_vieninieku_skaits = 0
# vieninieku_skaits = 0
# bija_nulle = False
# for char in s:
#     if char == "0":
#         bija_nulle = True

#     if char == "1" and bija_nulle:
#         vieninieku_skaits += 1
#     elif char == "0" and vieninieku_skaits > 0:
#         if vieninieku_skaits > max_vieninieku_skaits:
#             max_vieninieku_skaits = vieninieku_skaits
#         vieninieku_skaits = 0

# print(max_vieninieku_skaits)

# 2. no FV

# s = "aaabbcaaa" # -> a3b2c1a3
# result = ""
# current = ""
# current_count = 0
# for char in s:
#     if char == current:
#         current_count += 1
#     else:
#         if current_count > 0:
#             result += current + str(current_count)
#         current = char
#         current_count = 1

# result += current + str(current_count)
# print(result)
