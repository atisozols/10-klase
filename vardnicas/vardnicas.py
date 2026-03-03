# ============================================================
# 1. KAS IR VĀRDNĪCA (MAP/HASHMAP/DICTIONARY)
# ============================================================
# Vārdnīca glabā datus kā "atslēga: vērtība" pārus.
# Atslēgām jābūt unikālām.
#
# Piemērs:
# skolēns = {
#     "vārds": "Anna",
#     "vecums": 16,
#     "vid_vertejums": 8.4
# }


# ============================================================
# 2. IZVEIDE UN PIEKĻUVE
# ============================================================

# Tukša vārdnīca
v = {}

# Ar datiem
pilsetas = {
    "Riga": 605000,
    "Liepaja": 67000,
    "Cesis": 15000,
}

# Piekļuve pēc atslēgas
# print(pilsetas["Riga"])       # 605000

# Drošāka piekļuve ar get()
# print(pilsetas.get("Ventspils"))      # None
# print(pilsetas.get("Tukums", 0))   # 0


# ============================================================
# 3. PIEVIENOŠANA, MAIŅA, DZĒŠANA
# ============================================================

# Pievienot jaunu pāri
# pilsetas["Valmiera"] = 23000
# pilsetas["Valmiera"] = 25000

# print(pilsetas.get("Valmiera"))

# # Mainīt esošu vērtību
# pilsetas["Riga"] = 606000

# Dzēst pēc atslēgas
# del pilsetas["Cesis"]

# Izņemt un saņemt vērtību
# skaits = pilsetas.pop("Liepaja")  # 67000
# print(skaits)
# print(pilsetas)

# Pārbaude, vai atslēga eksistē
# print("Riga" in pilsetas)     # True
# print("Daugavpils" in pilsetas)


# ============================================================
# 4. ITERĒŠANA (for) PA VĀRDNĪCU
# ============================================================

# Tikai atslēgas
# for key in pilsetas:
#     print(key)

# Tikai vērtības
# for value in pilsetas.values():
#     print(value)

# Atslēga + vērtība
# for key, value in pilsetas.items():
#     print(key, value)

# Atslēga + vērtība alternatīva
# for key in pilsetas:
#     print(key, pilsetas[key])


# ============================================================
# 5. NODERĪGAS METODES
# ============================================================

# Garums
# print(len(pilsetas))

# Visas atslēgas / vērtības / pāri
# print(list(pilsetas.keys()))
# print(list(pilsetas.values()))
# print(list(pilsetas.items()))

# Apvienošana / atjaunošana
# pilsetas.update({"Talsi": 9000, "Kuldiga": 10000})

# Notīrīt vārdnīcu
# pilsetas.clear()


# ============================================================
# 6. PRAKTISKI PARAUGI
# ============================================================

# 6.1 Simbolu skaitīšana virknē
# teksts = "programmesana"
# skaits = {}
# for ch in teksts:
#     skaits[ch] = skaits.get(ch, 0) + 1
#     print(ch, skaits)
# print(skaits)


# 6.2 Vārdu biežums tekstā
# text = "suns kakis suns putns kakis suns"
# freq = {}
# for vards in text.split():
#     freq[vards] = freq.get(vards, 0) + 1
# print(freq)


# 6.3 Grupēšana pēc pirmā burta
# vardi = ["Anna", "Andris", "Baiba", "Bruno", "Cecilia"]
# grupas = {}
# for vards in vardi:
#     burts = vards[0]
#     if burts not in grupas:
#         grupas[burts] = []
#     grupas[burts].append(vards)
# print(grupas)


# 6.4 Vārdnīca vārdnīcā
# studenti = {
#     "Anna": {"mat": 8, "eng": 9},
#     "Juris": {"mat": 6, "eng": 7},
# }
# print(studenti["Anna"]["mat"])  # 8


# ============================================================
# 7. BIEŽĀKĀS KĻŪDAS
# ============================================================
# 1) Piekļūt neeksistējošai atslēgai ar d[key] (KeyError).
#    Lieto get() vai pārbaudi "if key in d".
# 2) Sajaukt saraksta indeksu ar vārdnīcas atslēgu.
# 3) Mainīt vārdnīcu iterācijas laikā pa to pašu vārdnīcu.
# 4) Aizmirst, ka atslēgām jābūt nemaināmiem tipiem
#    (piem., str, int, tuple; nevis list).


# ============================================================
# 8. UZDEVUMI
# ============================================================

# 1. uzdevums - pamatdarbības
# Izveido vārdnīcu "sports", kurā ir vismaz 4 sporta veidi un
# katram atbilst spēlētāju skaits laukumā.
# Izvadi:
# - visu vārdnīcu,
# - tikai atslēgas,
# - tikai vērtības.

# sports = {
#     "futbols": 11,
#     "hokejs": 5,
#     "volejbols": 6,
#     "florbols": 5
# }

# print(sports)
# print(list(sports.keys()))
# print(list(sports.values()))

# 2. uzdevums - pievienošana un labošana
# Dotajai vārdnīcai pievieno vienu jaunu pāri un vienai esošai atslēgai
# nomaini vērtību. Pēc tam izdzēs vienu ierakstu.

# sports = {
#     "futbols": 11,
#     "hokejs": 5,
#     "volejbols": 6,
#     "florbols": 5
# }

# sports["teniss"] = 1
# sports["florbols"] = 6
# print(sports)

# 3. uzdevums - droša meklēšana
# Lietotājs ievada pilsētas nosaukumu.
# Ja pilsēta ir vārdnīcā, izvadi iedzīvotāju skaitu.
# Ja nav, izvadi "Nav datu".
# (Ieteikums: get())

# meklejama_pilseta = input("ievadi pilsētu, lai iegūtu iedzīvotāju skaitu: ")

# 1. variants
# print(pilsetas.get(meklejama_pilseta, "Nav datu"))

# 2. variants
# if meklejama_pilseta in pilsetas:
#     print(pilsetas[meklejama_pilseta])
# else:
#     print("Nav datu")


# 4. uzdevums - summa un vidējā vērtība
# Dota vārdnīca, kuras atslēga ir prece, bet vērtība ir daudzums.
# Aprēķini:
# - kopējo daudzumu;
# - vidējo daudzumu uz vienu preci.

preces = {
    "maize": 4,
    "piens": 5,
    "siers": 2
}

summa = 0
for prece, skaits in preces.items():
    summa += skaits

print(len(preces), summa, summa/len(preces))



# 5. uzdevums - maksimālā vērtība
# Atrodi to atslēgu, kurai ir lielākā vērtība vārdnīcā.
# Ja ir vairākas vienādas maksimālās vērtības, pietiek ar pirmo atrasto.


# 6. uzdevums - filtrēta vārdnīca
# Izveido jaunu vārdnīcu, kurā paliek tikai tie pāri,
# kuru vērtība ir >= 10.


# 7. uzdevums - burtu biežums
# Lietotājs ievada tekstu.
# Saskaiti, cik reizes katrs burts parādās (ignorē atstarpes,
# lielos/mazos burtus uzskati vienādi).


# 8. uzdevums - vārdu biežums
# Lietotājs ievada teikumu.
# Izveido vārdnīcu, kas glabā vārdu parādīšanās skaitu.
# Izvadi vārdus un to biežumu.


# 9. uzdevums - top 3 vārdi
# Pamatojoties uz iepriekšējo uzdevumu, atrodi 3 biežākos vārdus.
# Ja vārdu ir mazāk par 3, izvadi tik, cik ir.


# 10. uzdevums - invertēt vārdnīcu
# Dota vārdnīca ar unikālām vērtībām.
# Izveido apgrieztu vārdnīcu:
# vecās vērtības kļūst par atslēgām, vecās atslēgas par vērtībām.


# 11. uzdevums - apvienot divas vārdnīcas
# Dotas vārdnīcas d1 un d2 ar skaitliskām vērtībām.
# Izveido vienu vārdnīcu:
# - ja atslēga ir tikai vienā vārdnīcā, paņem tās vērtību;
# - ja atslēga ir abās, vērtības saskaiti.


# 12. uzdevums - skolēnu atzīmes
# Izveido ligzdotu vārdnīcu:
# students -> {"mat": ..., "eng": ..., "prog": ...}
# Izvadi katra skolēna vidējo atzīmi.


# 13. uzdevums - labākais students
# Izmantojot iepriekšējo struktūru, atrodi skolēnu ar lielāko
# vidējo atzīmi.


# 14. uzdevums - telefongrāmata
# Izveido programmu, kas cikliski piedāvā darbības:
# "pievienot", "meklēt", "dzēst", "izvadīt visu", "beigt".
# Datus glabā vārdnīcā (vārds -> telefons).


# 15. uzdevums - pirmais neatkārtotais simbols
# Dota simbolu virkne.
# Ar vārdnīcas palīdzību atrodi pirmo simbolu,
# kas tekstā parādās tieši 1 reizi.
# Ja tāda nav, izvadi "Nav".


# 16. uzdevums - anagrammu pārbaude
# Dotas divas virknes.
# Pārbaudi, vai tās ir anagrammas
# (vienāds simbolu biežums, ignorējot atstarpes un reģistru).


# 17. uzdevums - uzkrājoša statistika
# Lietotājs ievada skaitļus, līdz ievada 0.
# Uzturi vārdnīcu ar statistiku:
# {"count": ..., "sum": ..., "min": ..., "max": ...}
# Pēc ievades izvadi statistiku.


# 18. uzdevums - sarežģītākais (pirmais algoritmiskais)
# Dots saraksts ar skaitliem.
# Atrodi garāko apakšsarakstu, kurā visi elementi ir dažādi.
# Norāde: lieto vārdnīcu, lai glabātu pēdējo pozīciju katram elementam.
