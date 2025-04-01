sports = {
    "futbols": 6,
    "hokejs": 7,
    "basits": 3
    }

# print(sports.get("volejbols", 0))

# sports["teniss"] = 2
# sports["futbols"] = 10
# del sports["basits"]

# for key, value in sports.items():
#     print(f"Sporta veids: {key}, Spēlētāju skaits: {value}")

# for key in sports:
#     print(f"Sporta veids: {key}, Spēlētāju skaits: {sports[key]}")

# print(sports)

def filtret_sportus(vardnica):
    new_vardnica = {}

    for key, value in vardnica.items():
        if value > 5:
            new_vardnica[key] = value

    for key in vardnica:
        if vardnica[key] > 5:
            new_vardnica[key] = vardnica[key]

    return new_vardnica

# 82. Ievadīts teksts. Programma nosaka, cik procentuāli daudz ir katrs no tekstā sastopamajiem burtiem.

text = "Tāpat valdībā konceptuāli atbalstīts ministrijas priekšlikums palielināt minimālo ieņēmumu prasību konvencionālajām saimniecībām līdz 450 eiro no hektāra un bioloģiskajām saimniecībām – līdz 270 eiro no hektāra. Savukārt, ja  lauksaimniecības cenu indekss vismaz trīs gadus pēc kārtas ir bijis augstāks par 20% salīdzinājumā pret 2024. gadu, tad Zemkopības ministrija izvērtēs minimālo ieņēmumu kritērijus, sākot no 2029./2030. saimnieciskā gada."
text = text.lower()

counts = {}
total = 0

for char in text:
    if char.isalpha():
        total += 1
        # mēģinām dabūt vērtību, kas ir pretī burtam "t", ja tāda nav, dabūsim 0
        # counts["t"] = counts.get("t", 0) + 1     
        # counts[char] = counts.get(char, 0) + 1
        counts[char] = text.count(char)

for key in counts:
    print(key, round(counts[key]/total*100, 2))

# 83. Tekstā atrast top 3 biežāk sastopamos vārdus.

# 84. 
