# vards_uzvards = input("vārds, uzvārds: ").strip()

# saraksts = vards_uzvards.split()

# print(f"{saraksts[1]}, {saraksts[0]}")

# answer = input("Do you agree? (yes/no): ")

# answer = answer.strip().upper()

# if answer == "YES":
#     print("Accepted")
# else:
#     print("Rejected")

# text = input("Write a comment: ")

# words_to_replace = ["bad", "good"]

# for word in words_to_replace:
#     text = text.replace(word, "***")

# print(text)

# teikums = input("Ievadiet teikumu: ")

# teikums_saraksts = teikums.split() # ['drīz', 'beigsies', 'nodarbība', 'šodien']

# print(len(teikums_saraksts)) 
# print(teikums_saraksts[0])


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



from itertools import count


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

s = "aaabbcaaa" # -> a3b2c1a3
result = ""
current = ""
current_count = 0
for char in s:
    if char == current:
        current_count += 1
    else:
        if current_count > 0:
            result += current + str(current_count)
        current = char
        current_count = 1

result += current + str(current_count)
print(result)
