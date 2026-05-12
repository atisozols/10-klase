# Pārbaudes darbs

**Tēma:** Klases, atribūti un metodes

## 1. uzdevums — `Trapece`

Ģeometriska figūra ar divām paralēlām malām.

**Atribūti:** `a`, `b` (paralēlās malas), `c`, `d` (sānu malas), `augstums`.

**Metodes:**

- `laukums()` — atgriež trapeces laukumu pēc formulas `(a + b) * augstums / 2`.
- `perimetrs()` — atgriež visu četru malu summu.
- `ir_vienadsanu()` — atgriež `True`, ja sānu malas `c` un `d` ir vienādas.

**Piemēri:**

```python
t = Trapece(6, 4, 3, 3, 2)
t.laukums()         # -> 10.0
t.perimetrs()       # -> 16
t.ir_vienadsanu()   # -> True

t2 = Trapece(8, 5, 3, 4, 2)
t2.ir_vienadsanu()  # -> False
```

---

## 2. uzdevums — `Dalskaitlis`

Daļskaitlis ar skaitītāju un saucēju (piem., `3/4`).

**Atribūti:** `skaititajs`, `saucejs`.

**Metodes:**

- `decimalvertiba()` — atgriež daļskaitļa decimālvērtību (`skaititajs / saucejs`).
- `ir_pareiza()` — atgriež `True`, ja `|skaititajs| < |saucejs|` (īsta daļa).
- `apvert()` — atgriež **jaunu** `Dalskaitlis` objektu, kuram skaitītājs un saucējs ir samainīti vietām.
- `pieskaitit(cits)` — atgriež **jaunu** `Dalskaitlis` objektu, kas ir abu daļskaitļu summa.
  Formula: `a/b + c/d = (a*d + c*b) / (b*d)`.

**Piemēri:**

```python
d = Dalskaitlis(3, 4)
d.decimalvertiba()      # -> 0.75
d.ir_pareiza()          # -> True

d2 = Dalskaitlis(7, 5)
d2.ir_pareiza()         # -> False

d3 = d.apvert()
d3.skaititajs, d3.saucejs   # -> 4, 3

d4 = Dalskaitlis(1, 2)
d5 = Dalskaitlis(1, 3)
s = d4.pieskaitit(d5)
s.skaititajs, s.saucejs     # -> 5, 6
```

---

## 3. uzdevums — `LinearaFunkcija`

Lineāra funkcija formā `y = k * x + b`.

**Atribūti:** `k`, `b`.

**Metodes:**

- `vertiba(x)` — atgriež funkcijas vērtību punktā `x`.
- `nulles_punkts()` — atgriež `x` vērtību, kurā `y = 0` (t.i., `-b / k`).
  Ja `k == 0`, atgriež `None`.
- `ir_augosa()` — atgriež `True`, ja `k > 0`.

**Piemēri:**

```python
f = LinearaFunkcija(2, -4)
f.vertiba(3)            # -> 2
f.vertiba(0)            # -> -4
f.nulles_punkts()       # -> 2.0
f.ir_augosa()           # -> True

g = LinearaFunkcija(0, 5)
g.nulles_punkts()       # -> None
g.ir_augosa()           # -> False
```

---

## 4. uzdevums — `Darbinieks`

Uzņēmuma darbinieks ar darba laiku.

**Atribūti:** `vards`, `amats`, `stundas_likme`, `nostradatas_stundas` (sākumā 0).

**Metodes:**

- `pievienot_stundas(s)` — pieskaita `s` stundas pie `nostradatas_stundas`.
- `alga()` — atgriež algu (`stundas_likme * nostradatas_stundas`).
- `ir_virsstundas()` — atgriež `True`, ja nostrādātas vairāk par 40 stundām.
- `apraksts()` — atgriež tekstu formātā:
  `"Anna (programmētājs) — 25.00 EUR"` (alga ar 2 cipariem aiz komata).

**Piemēri:**

```python
d = Darbinieks("Anna", "programmētājs", 5.0)
d.pievienot_stundas(20)
d.pievienot_stundas(25)
d.alga()                # -> 225.0
d.ir_virsstundas()      # -> True
d.apraksts()            # -> "Anna (programmētājs) — 225.00 EUR"
```

---

## 5. uzdevums — `Restorans`

Restorāna pasūtījumu sistēma.

**Atribūti:** `nosaukums`, `pasutijumi` (vārdnīca `{ediens: skaits}`).

**Metodes:**

- `pasutit(ediens, skaits)` — pievieno `skaits` porcijas dotajam ēdienam.
  Ja ēdiens jau ir vārdnīcā, palielina esošo skaitu.
- `kopejais_skaits()` — atgriež visu pasūtīto porciju summu.
- `popularakais()` — atgriež ēdiena nosaukumu, kas pasūtīts visvairāk.
- `ir_pasutits(ediens)` — atgriež `True`, ja ēdiens ir pasūtījumos.

**Piemēri:**

```python
r = Restorans("Lido")
r.pasutit("zupa", 2)
r.pasutit("karbonade", 3)
r.pasutit("zupa", 1)
r.kopejais_skaits()         # -> 6
r.popularakais()            # -> "karbonade"
r.ir_pasutits("zupa")       # -> True
r.ir_pasutits("salati")     # -> False
```

---

## 6. uzdevums — `Datums`

Kalendāra datums ar pārbaudēm.

**Atribūti:** `diena`, `menesis`, `gads`.

**Metodes:**

- `ir_derigs()` — atgriež `True`, ja datums ir korekts:
  - `menesis` ir no 1 līdz 12,
  - `diena` ir no 1 līdz attiecīgā mēneša pēdējam datumam.
  - Mēnešu garumi: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
  - (Garo gadu pārbaude **nav** jāveic.)
- `nakamais()` — palielina datumu par vienu dienu (pareizi pārejot starp mēnešiem un gadiem).
- `teksts()` — atgriež datumu formātā `"DD.MM.YYYY"`,
  piemēram, `"05.03.2026"` (ar nullēm priekšā, ja vajag).

**Piemēri:**

```python
d = Datums(5, 3, 2026)
d.ir_derigs()           # -> True
d.teksts()              # -> "05.03.2026"

d2 = Datums(31, 1, 2026)
d2.nakamais()
d2.teksts()             # -> "01.02.2026"

d3 = Datums(31, 12, 2026)
d3.nakamais()
d3.teksts()             # -> "01.01.2027"

d4 = Datums(30, 2, 2026)
d4.ir_derigs()          # -> False
```
