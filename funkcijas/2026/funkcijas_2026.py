# https://cscircles.cemc.uwaterloo.ca/visualize
# ============================================================
# FUNKCIJAS 2026
# ============================================================
# Funkcija ir koda bloks, kuru var izsaukt vairākas reizes.
# Tā palīdz:
# - izvairīties no viena un tā paša koda rakstīšanas atkārtoti;
# - sadalīt programmu mazākos, saprotamākos soļos;
# - vieglāk testēt programmas loģiku.
#
# Vispārīgā forma:
#
# def nosaukums(parametrs1, parametrs2):
#     darbības
#     return rezultāts
#
# Svarīgi:
# 1) parametri ir ievades dati funkcijai;
# 2) return atgriež vērtību;
# 3) print tikai izvada uz ekrāna;
# 4) viena programma bieži sastāv no vairākām mazām funkcijām.


# ============================================================
# 1. PAMATI
# ============================================================

def sasveicinies(vards = "Nezināmais"):
    print(f"Sveiks, {vards}")

def pilns_vards(vards, uzvards):
    return f"{uzvards}, {vards}"
    

def kvadrats(n):
    return n * n


def ir_para(sk):
    return sk % 2 == 0



# Piemēri:
# sasveicinies()
# print(pilns_vards("Anna", "Kalnina"))   # Kalnina, Anna
# print(kvadrats(6))                      # 36
# print(ir_para(16))                      # False


# ============================================================
# 2. PRINT UN RETURN NAV VIENS UN TAS PATS
# ============================================================

# def izvada_summu(a, b):
#     print(a + b)


# def atgriez_summu(a, b):
#     return a + b


# izvada_summu(4, 5)         # uz ekrāna parādīsies 9
# x = atgriez_summu(4, 5)    # x glabās vērtību 9
# print(x * 2)               # 18


# ============================================================
# 3. DAŽI PARAUGI
# ============================================================

def teksts_lielajiem_burtiem(text):
    return text.upper()


def saraksta_summa(s):
    summa = 0
    for elem in s:
        summa += elem
    return summa


def dubultots_saraksts(s):
    result = []
    for elem in s:
        result.append(elem * 2)
    return result


def simbolu_biezums(text):
    skaits = {}
    for simbols in text:
        if simbols != " ":
            skaits[simbols] = skaits.get(simbols, 0) + 1
    return skaits


# print(teksts_lielajiem_burtiem("python"))
# print(saraksta_summa([4, 7, 2]))          # 13
# print(dubultots_saraksts([1, 3, 5]))      # [2, 6, 10]
# print(simbolu_biezums("anna"))            # {'a': 2, 'n': 2}


# ============================================================
# 4. PADOMS RISINOT UZDEVUMUS
# ============================================================
# Katrā uzdevumā mēģini:
# 1) uzrakstīt funkciju,
# 2) pārbaudīt to ar 2-3 piemēriem,
# 3) tikai pēc tam izmantot input() un print(), ja tas ir vajadzīgs.
#
# Zemāk daudzām funkcijām ir pass.
# Tas ir vietturis: programma palaidīsies, bet loģika tev vēl jāuzraksta.


# ============================================================
# 5. UZDEVUMI PAR FUNKCIJĀM — SARAKSTI
# Adaptēts no 10-klase/saraksti
# ============================================================

def elementi_virs_videja(s):
    result = []
    avg = sum(s)/len(s)
    for elem in s:
        if elem > avg:
            result.append(elem)
    return result


def bez_dublikatiem(s):
    result = []
    for elem in s:
        if elem not in result:
            result.append(elem)
    return result


def saraksts_par_skaitli(cipari):
    # Dots saraksts, kur katrs elements ir cipars no 0 līdz 9.
    # Izveido un atgriez vienu veselu skaitli.
    # Piemērs: [6, 1, 2, 3] -> 6123
    skaitlis = 0
    for cipars in cipari:
        skaitlis = skaitlis * 10 + cipars
    return skaitlis


def garaka_vienadu_serija(s):
    max_skaits = 0
    max_vertiba = 0
    skaits = 0
    vertiba = 0
    for elem in s:
        if elem == vertiba:
            skaits += 1
            if skaits > max_skaits:
                max_skaits = skaits
                max_vertiba = vertiba
        else:
            skaits = 1
            vertiba = elem
    
    return (max_skaits, max_vertiba)


def garakais_augsosais_apaksaraksts(s):
    garaka_apaksvirkne = []
    apaksvirkne = []
    for elem in s:
        if len(apaksvirkne) > 0:
            if elem > apaksvirkne[-1]:
                apaksvirkne.append(elem)
            else:
                if len(apaksvirkne) > len(garaka_apaksvirkne):
                    garaka_apaksvirkne = apaksvirkne.copy()
                apaksvirkne = [elem]
        else:
            apaksvirkne.append(elem)

        if len(apaksvirkne) > len(garaka_apaksvirkne):
            garaka_apaksvirkne = apaksvirkne.copy()

    return (len(garaka_apaksvirkne), garaka_apaksvirkne)

# ============================================================
# 6. UZDEVUMI PAR FUNKCIJĀM — SIMBOLU VIRKNES
# Adaptēts no 10-klase/simbolu_virknes
# ============================================================

def masket_ciparus(text):
    result = text
    cipari = "0123456789"
    for cipars in cipari:
        result = result.replace(cipars, "#")
    return result


def apgriezt_vardu_secibu(text):
    words = text.strip()
    words = words.split()
    words.reverse()
    return " ".join(words)


def popularakais_simbols(text):
    vardnica = {}
    for char in text:
        vardnica[char] = vardnica.get(char, 0) + 1

    biezhakais = ""
    skaits = 0
    for key, value in vardnica.items():
        if value > skaits:
            biezhakais = key
            skaits = value
    return (biezhakais, skaits)


def garakais_tirais_vards(text):
    words = text.split()
    longest = ""

    for word in words:
        if word.isalpha() and len(word) > len(longest):
            longest = word
    
    return longest


def saspiest_vardus(text):
    result = ""
    current = ""
    current_count = 0

    for word in text.split():
        if word == current:
            current_count += 1
        else:
            if current_count > 0:
                result += current + str(current_count)
            current = word
            current_count = 1

    result += current + str(current_count)

    return result


# ============================================================
# 7. UZDEVUMI PAR FUNKCIJĀM — VĀRDNĪCAS
# Adaptēts no 10-klase/vardnicas
# ============================================================

def kabineta_numurs(kabineti, prieksmets):
    if prieksmets in kabineti:
        return kabineti[prieksmets]
    else:
        return "Nav datu"

# vardnica = {"Matemātika": 24, "Programmēšana": 60}
# atslega = "Matemātika"

# print(kabineta_numurs(vardnica, atslega))

def vardu_pirmo_burtu_biezums(text):
    result = {}
    for word in text.split():
        pirmais_burts = word[0].lower()
        result[pirmais_burts] = result.get(pirmais_burts, 0) + 1

    return result


# v = vardu_pirmo_burtu_biezums("programmesana ir mans milakais prieksmets")
# print(vardu_pirmo_burtu_biezums("vidusskola ir labakais laiks"))


def aukstas_pilsetas(temperaturas):
    # Izveido jaunu vārdnīcu, kur paliek tikai pilsētas ar temperatūru < 0.
    #
    # Atgriez:
    # 1) jauno vārdnīcu,
    # 2) pilsētu skaitu,
    # 3) vidējo temperatūru.
    #
    # Ja nav nevienas aukstas pilsētas, vidējās vērtības vietā atgriez None.
    pass


def rezultatu_izmainas(pirmais, otrais):
    # Apskati tikai skolēnus, kuri ir abās vārdnīcās.
    # Izveido jaunu vārdnīcu, kur vērtība ir otrais - pirmais.
    #
    # Atgriez:
    # 1) izmaiņu vārdnīcu,
    # 2) cik uzlabojās,
    # 3) cik pasliktinājās,
    # 4) cik palika bez izmaiņām.
    pass


def balsojuma_rezultats(balsis):
    record = 0
    record_holder = ""
    result = {}

    for balss in balsis:
        result[balss] = result.get(balss, 0) + 1
        if result[balss] > record:
            record = result[balss]
            record_holder = balss

    return {record_holder: record}

# Test examples for balsojuma_rezultats
# print(balsojuma_rezultats(["Anna", "Juris", "Anna", "Anna", "Juris"]))  # {'Anna': 3}
# print(balsojuma_rezultats(["A", "B", "C", "A", "B", "A"]))  # {'A': 3}
# print(balsojuma_rezultats(["Atis", "Atis", "Kristers", "Kristers", "Atis"]))  # {'Atis': 3}
# print(balsojuma_rezultats(["viens", "divi", "viens", "divi", "viens", "viens"]))  # {'viens': 4}

# ============================================================
# 8. PAPILDU IDEJA
# ============================================================
# Paņem jebkuru veco uzdevumu un sadali to 2 vai 3 funkcijās.
# Piemēram:
# - viena funkcija attīra ievadi,
# - viena funkcija izdara galveno aprēķinu,
# - viena funkcija noformē rezultātu.
#
# Tas ir labs solis no "viena gara skripta" uz sakārtotu programmu.

# Piemērs 1: paroles stipruma pārbaudītājs
# (adaptēts no simbolu_virknes/12. uzdevums)
# Oriģināli bija viens garš skripts — tagad sadalīts 3 funkcijās.

def analizet_paroli(parole):
    # saskaita atstarpes, lielos burtus un ciparus
    atstarpes = 0
    lielie = 0
    cipari = 0
    for simbols in parole:
        if simbols == " ":
            atstarpes += 1
        if simbols.isupper():
            lielie += 1
        if simbols.isdigit():
            cipari += 1
    return {"atstarpes": atstarpes, "lielie": lielie, "cipari": cipari}


def ir_stipra(parole):
    # atgriež True, ja parole atbilst visiem kritērijiem
    analīze = analizet_paroli(parole)
    return (len(parole) > 7
            and analīze["atstarpes"] == 0
            and analīze["lielie"] > 0
            and analīze["cipari"] > 0)


def formatet_paroles_rezultatu(stipra):
    # atgriež cilvēkam lasāmu tekstu
    if stipra:
        return "Strong"
    return "Weak"

parole = input("Ievadi paroli: ")
print(formatet_paroles_rezultatu(ir_stipra(parole)))

# Piemērs 2: lietotājs ievada tekstu un programma atrod biežāko vārdu

def attirit_tekstu(text):
    # noņem pieturzīmes, pārveido mazajos burtos
    pieturzimes = ".,!?;:'\"-()[]{}/"
    rezultats = ""
    for char in text.lower():
        if char not in pieturzimes:
            rezultats += char
    return rezultats


def saskaitit_vardus(text):
    # atgriež vārdnīcu ar vārdu biežumu
    tirais_teksts = attirit_tekstu(text)
    vardnica = {}
    for vards in tirais_teksts.split():
        vardnica[vards] = vardnica.get(vards, 0) + 1
    return vardnica


def atrast_biezako(vardnica):
    # atgriež biežāko vārdu un tā skaitu
    biezakais = ""
    skaits = 0
    for vards, biežums in vardnica.items():
        if biežums > skaits:
            biezakais = vards
            skaits = biežums
    return (biezakais, skaits)


def formatet_rezultatu(biezakais, skaits):
    # atgriež cilvēkam lasāmu tekstu
    return f"Biežākais vārds ir '{biezakais}' ar {skaits} atkārtojumiem."

text = input("Ievadi tekstu: ")
vardnica = saskaitit_vardus(text)
biezakais, skaits = atrast_biezako(vardnica)
print(formatet_rezultatu(biezakais, skaits))
