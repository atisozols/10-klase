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


def bez_duplikatiem(s):
    # Atgriez jaunu sarakstu, kur katra vērtība parādās tikai vienu reizi,
    # saglabājot pirmās parādīšanās secību.
    # Piemērs: [3, 1, 3, 2, 1] -> [3, 1, 2]
    pass


def saraksts_par_skaitli(cipari):
    # Dots saraksts, kur katrs elements ir cipars no 0 līdz 9.
    # Izveido un atgriez vienu veselu skaitli.
    # Piemērs: [6, 1, 2, 3] -> 6123
    pass


def garaka_vienadu_serija(s):
    # Atgriez garākās vienādu blakus elementu sērijas garumu un vērtību.
    # Ja ir vairākas vienāda garuma sērijas, atgriez pirmo.
    # Piemērs: [4, 4, 4, 2, 2, 9] -> (3, 4)
    pass


def garakais_augsosais_apaksaraksts(s):
    # Atgriez garumu un pašu garāko stingri augošo apakšsarakstu.
    # Ja ir vairāki vienāda garuma, atgriez pirmo.
    # Piemērs: [1, 2, 5, 3, 4, 8] -> (3, [1, 2, 5])
    pass


# ============================================================
# 6. UZDEVUMI PAR FUNKCIJĀM — SIMBOLU VIRKNES
# Adaptēts no 10-klase/simbolu_virknes
# ============================================================

def masket_ciparus(text):
    # Aizstāj katru ciparu ar simbolu #.
    # Atgriez jauno tekstu un aizstāto ciparu skaitu.
    # Piemērs: "abc12x" -> ("abc##x", 2)
    pass


def apgriezt_vardu_secibu(text):
    # Noņem liekās atstarpes sākumā un beigās.
    # Atgriez tekstu ar apgrieztu vārdu secību.
    # Piemērs: " šodien ir labi " -> "labi ir šodien"
    pass


def popularakais_simbols(text):
    # Atrodi visbiežāk sastopamo simbolu, neskaitot atstarpes.
    # Ja ir vairāki vienādi, atgriez pirmo no tiem.
    # Atgriez simbolu un tā skaitu.
    # Piemērs: "abracadabra" -> ("a", 5)
    pass


def garakais_tirais_vards(text):
    # Atgriez garāko vārdu, kas satur tikai burtus.
    # Ja ir vairāki vienāda garuma, atgriez pirmo.
    # Ja tāda nav, atgriez "Nav".
    # Piemērs: "abc 12xy hello3 world" -> "world"
    pass


def saspiest_vardus(text):
    # Saspied secīgi atkārtojošos vārdus:
    # "labi labi slikti" -> "labi2 slikti1"
    #
    # Atgriez:
    # 1) saspiesto tekstu,
    # 2) grupu skaitu,
    # 3) vārdu ar lielāko grupu,
    # 4) šīs grupas lielumu.
    pass


# ============================================================
# 7. UZDEVUMI PAR FUNKCIJĀM — VĀRDNĪCAS
# Adaptēts no 10-klase/vardnicas
# ============================================================

def kabineta_numurs(kabineti, prieksmets):
    # Dota vārdnīca ar formu:
    # {"Matematika": 214, "Biologija": 306}
    #
    # Atgriez kabineta numuru, ja priekšmets ir vārdnīcā.
    # Ja nav, atgriez "Nav datu".
    pass


def vardu_pirmo_burtu_biezums(text):
    # Sadalī tekstu vārdos.
    # Izveido vārdnīcu, kas glabā katra vārda pirmā burta skaitu.
    # Lielos un mazos burtus uzskati vienādi.
    #
    # Atgriez:
    # 1) biežumu vārdnīcu,
    # 2) visbiežāko pirmo burtu,
    # 3) tā skaitu.
    #
    # Piemērs:
    # "Anna lasa avenes ar Bruno" -> ({"a": 3, "l": 1, "b": 1}, "a", 3)
    pass


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
    # Dots kandidātu saraksts, piemēram:
    # ["Anna", "Juris", "Anna", "Liva", "Anna"]
    #
    # Izveido vārdnīcu ar balsu skaitu katram kandidātam.
    #
    # Atgriez:
    # 1) balsu vārdnīcu,
    # 2) kopējo balsu skaitu,
    # 3) uzvarētāja vārdu,
    # 4) uzvarētāja balsu skaitu.
    #
    # Ja saraksts ir tukšs, vari atgriezt ({}, 0, None, 0)
    pass


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
