# https://cscircles.cemc.uwaterloo.ca/visualize
# ============================================================
# KLASES 2026
# ============================================================
# Klase ir veids, kā aprakstīt objekta tipu.
# Objekts ir konkrēts šī tipa piemērs ar savām vērtībām.
#
# Klases palīdz:
# - savākt kopā datus un darbības, kas ar tiem strādā;
# - izveidot vairākus objektus, kas dalās ar vienu uzbūvi;
# - veidot programmu, kas ir vieglāk paplašināma un saprotama.
#
# Salīdzinājumam:
# - saraksts glabā vairākas vērtības pa indeksiem;
# - vārdnīca glabā atslēga: vērtība pārus;
# - klase apraksta objektu ar atribūtiem un metodēm.
#
# Vispārīgā forma:
#
# class Nosaukums:
#     def __init__(self, parametrs1, parametrs2):
#         self.atribuuts1 = parametrs1
#         self.atribuuts2 = parametrs2
#
#     def metode(self):
#         return self.atribuuts1
#
# Svarīgi:
# 1) __init__ ir konstruktors — izpildās, kad veido jaunu objektu;
# 2) self ir pats objekts — bez tā metode nezina, ar kuru objektu strādā;
# 3) atribūti tiek glabāti objektā ar self.nosaukums = vertiba;
# 4) metodes ir funkcijas, kas strādā ar objekta datiem.


# ============================================================
# 1. PAMATI
# ============================================================

class Dziesma:
    def __init__(self, nosaukums, izpilditajs, ilgums):
        self.nosaukums = nosaukums
        self.izpilditajs = izpilditajs
        self.ilgums = ilgums

    def apraksts(self):
        return f"{self.izpilditajs} - {self.nosaukums} ({self.ilgums}s)"


# Piemēri:
# d = Dziesma("Saule", "Prāta Vētra", 215)
# print(d.nosaukums)       # Saule
# print(d.izpilditajs)     # Prāta Vētra
# print(d.apraksts())      # Prāta Vētra - Saule (215s)


# ============================================================
# 2. VAIRĀKI OBJEKTI NO VIENAS KLASES
# ============================================================
# Klase ir kā "plāns" vai "veidne".
# Objekts ir konkrēts "īpašums", kas izveidots pēc šī plāna.
# Katram objektam ir savi atribūti.

# d1 = Dziesma("Saule", "Prāta Vētra", 215)
# d2 = Dziesma("Dzimtene", "Pērkons", 180)
# print(d1.nosaukums, d1.ilgums)    # Saule 215
# print(d2.nosaukums, d2.ilgums)    # Dzimtene 180
# print(d1.apraksts())
# print(d2.apraksts())


# ============================================================
# 3. ATRIBŪTI UN METODES
# ============================================================

class Taisnsturis:
    def __init__(self, garums, platums):
        self.garums = garums
        self.platums = platums

    def laukums(self):
        return self.garums * self.platums

    def perimetrs(self):
        return 2 * (self.garums + self.platums)

    def ir_kvadrats(self):
        return self.garums == self.platums


# t = Taisnsturis(5, 3)
# print(t.laukums())       # 15
# print(t.perimetrs())     # 16
# print(t.ir_kvadrats())   # False
#
# k = Taisnsturis(4, 4)
# print(k.ir_kvadrats())   # True


# ============================================================
# 4. KLASE PRET VĀRDNĪCU
# ============================================================
# Vārdnīcā:
# skolens = {"vards": "Anna", "vecums": 16, "atzime": 8}
# print(skolens["vards"])
#
# Klasē:
# class Skolens:
#     def __init__(self, vards, vecums, atzime):
#         self.vards = vards
#         self.vecums = vecums
#         self.atzime = atzime
#
# anna = Skolens("Anna", 16, 8)
# print(anna.vards)
#
# Abi strādā — bet klase dod:
# 1) skaidru struktūru (vienmēr tie paši lauki);
# 2) metodes, kas strādā ar objekta datiem;
# 3) iespēju pārbaudīt un mainīt datus caur metodēm.


# ============================================================
# 5. DAŽI PARAUGI
# ============================================================

class Skolens:
    def __init__(self, vards, klase):
        self.vards = vards
        self.klase = klase
        self.atzimes = []

    def pievienot_atzimi(self, atzime):
        self.atzimes.append(atzime)

    def videja(self):
        if len(self.atzimes) == 0:
            return 0
        return sum(self.atzimes) / len(self.atzimes)

    def apraksts(self):
        return f"{self.vards} ({self.klase}. klase), vidējā: {self.videja():.1f}"


# a = Skolens("Anna", 10)
# a.pievienot_atzimi(8)
# a.pievienot_atzimi(9)
# a.pievienot_atzimi(7)
# print(a.videja())         # 8.0
# print(a.apraksts())       # Anna (10. klase), vidējā: 8.0


class Konts:
    def __init__(self, ipasnieks, atlikums=0):
        self.ipasnieks = ipasnieks
        self.atlikums = atlikums

    def iemaksat(self, summa):
        self.atlikums += summa

    def iznemt(self, summa):
        if summa > self.atlikums:
            return False
        self.atlikums -= summa
        return True


# k = Konts("Anna", 100)
# k.iemaksat(50)
# print(k.atlikums)        # 150
# print(k.iznemt(200))     # False
# print(k.iznemt(80))      # True
# print(k.atlikums)        # 70


class Punkts:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def attalums_lidz(self, cits):
        dx = self.x - cits.x
        dy = self.y - cits.y
        return (dx * dx + dy * dy) ** 0.5


# p1 = Punkts(0, 0)
# p2 = Punkts(3, 4)
# print(p1.attalums_lidz(p2))   # 5.0


# ============================================================
# 6. BIEŽĀKĀS KĻŪDAS
# ============================================================
# 1) Aizmirst self pirmajā parametrā metodēm.
# 2) Aizmirst self. pirms atribūta — tad top vietējais mainīgais,
#    kas pazūd, kad metode beidzas.
# 3) Pievienot atribūtu tieši klasē (ārpus __init__) — tad visi
#    objekti dalās ar vienu un to pašu vērtību.
# 4) Sajaukt klasi (plāns) ar objektu (konkrēts piemērs).
# 5) Mēģināt izsaukt metodi bez iekavām: t.laukums nevis t.laukums().


# ============================================================
# 7. PADOMS RISINOT UZDEVUMUS
# ============================================================
# Katrā uzdevumā mēģini:
# 1) uzrakstīt klasi ar __init__ un vajadzīgajām metodēm,
# 2) izveidot 2-3 objektus un pārbaudīt metodes,
# 3) tikai pēc tam saistīt ar input(), ja tas ir vajadzīgs.
#
# Zemāk daudzām klasēm ir pass.
# Tas ir vietturis: programma palaidīsies, bet loģika vēl jāuzraksta.


# ============================================================
# 8. UZDEVUMI — PAMATI
# ============================================================

class Gramata:
    # Atribūti: virsraksts, autors, lapas.
    # Metode apraksts() atgriež tekstu:
    # "{virsraksts} - {autors} ({lapas} lpp.)"
    #
    # Piemēri:
    # g = Gramata("Baltā grāmata", "Rainis", 240)
    # g.apraksts()  -> "Baltā grāmata - Rainis (240 lpp.)"
    pass


class Sunuks:
    # Atribūti: vards, vecums.
    # Metode ir_jauns() — atgriež True, ja vecums < 2.
    # Metode dzimsanas_diena() — palielina vecumu par 1.
    #
    # Piemēri:
    # s = Sunuks("Reksis", 1)
    # s.ir_jauns()          -> True
    # s.dzimsanas_diena()
    # s.vecums              -> 2
    # s.ir_jauns()          -> False
    pass


class Aplis:
    # Atribūts: radiuss.
    # Metode laukums() — atgriež apļa laukumu (pi * r * r).
    # Metode apkartmers() — atgriež apkārtmēru (2 * pi * r).
    # Izmanto pi = 3.14159.
    pass


# ============================================================
# 9. UZDEVUMI — PIEMĒROJUMI
# ============================================================

class IepirkumuGrozs:
    # Atribūts: preces (vārdnīca {nosaukums: cena}).
    # pievienot(nosaukums, cena) — pievieno preci.
    # iznemt(nosaukums) — noņem preci, ja tāda ir.
    # kopsumma() — atgriež visu cenu summu.
    # dargaka() — atgriež dārgākās preces nosaukumu.
    #
    # Piemēri:
    # g = IepirkumuGrozs()
    # g.pievienot("maize", 1.50)
    # g.pievienot("piens", 1.20)
    # g.pievienot("siers", 4.80)
    # g.kopsumma()     -> 7.5
    # g.dargaka()      -> "siers"
    pass


class Temperaturas:
    # Atribūts: merijumi (saraksts ar skaitļiem).
    # pievienot(t) — pievieno jaunu mērījumu.
    # videja() — atgriež vidējo temperatūru.
    # aukstaka() — atgriež mazāko vērtību.
    # siltaka() — atgriež lielāko vērtību.
    # aukstas_dienas() — atgriež, cik mērījumu ir < 0.
    pass


class Balsojums:
    # Atribūts: balsis (vārdnīca {kandidats: balsu_skaits}).
    # balsot(kandidats) — pieskaita vienu balsi.
    # uzvaretajs() — atgriež kandidātu ar lielāko balsu skaitu.
    # rezultati() — atgriež visu vārdnīcu ar balsīm.
    #
    # Piemēri:
    # b = Balsojums()
    # b.balsot("Anna")
    # b.balsot("Juris")
    # b.balsot("Anna")
    # b.uzvaretajs()    -> "Anna"
    # b.rezultati()     -> {"Anna": 2, "Juris": 1}
    pass


# ============================================================
# 10. UZDEVUMI — GRŪTĀKI
# ============================================================

class Laiks:
    # Atribūti: stundas, minutes.
    # __init__ parametros saņem stundas un minūtes.
    # pieskait_minutes(m) — pieskaita m minūtes.
    #   Ja minūtes pārsniedz 59, pareizi pārnes uz stundām.
    #   Ja stundas pārsniedz 23, sāk no 0 (kā pulkstenis).
    # teksts() — atgriež formātu "HH:MM" (piemēram, "09:05").
    #
    # Piemēri:
    # t = Laiks(9, 45)
    # t.pieskait_minutes(30)
    # t.teksts()        -> "10:15"
    # t = Laiks(23, 50)
    # t.pieskait_minutes(20)
    # t.teksts()        -> "00:10"
    pass


class Biblioteka:
    # Atribūts: gramatas (saraksts ar Gramata objektiem).
    # pievienot(gramata) — pievieno grāmatu sarakstam.
    # meklet_pec_autora(autors) — atgriež sarakstu ar visām
    #   tāda autora grāmatām.
    # kopeja_lapu_skaits() — atgriež visu grāmatu lapu summu.
    # biezakais_autors() — atgriež autoru, kura grāmatu ir visvairāk.
    pass


class Klase:
    # Atribūti: nosaukums (piem., "10A"), skoleni (saraksts ar Skolens objektiem).
    # pievienot_skolenu(skolens) — pievieno skolēnu sarakstam.
    # videja_atzime() — atgriež visas klases vidējo atzīmi
    #   (visu skolēnu visu atzīmju vidējā).
    # labakais_skolens() — atgriež skolēnu ar augstāko vidējo atzīmi.
    pass
