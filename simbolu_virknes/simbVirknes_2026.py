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
