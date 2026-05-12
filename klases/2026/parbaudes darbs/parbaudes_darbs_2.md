# Pārbaudes darbs (2. variants)

**Tēma:** Klases, atribūti un metodes

## 1. uzdevums — `Pikselis`

Krāsains pikselis ar trim krāsu kanāliem (sarkans, zaļš, zils).

**Atribūti:** `r`, `g`, `b` (katrs no 0 līdz 255).

**Metodes:**

- `spilgtums()` — atgriež trīs kanālu vidējo vērtību: `(r + g + b) / 3`.
- `ir_peleks()` — atgriež `True`, ja visi trīs kanāli ir vienādi.

**Piemēri:**

```python
p = Pikselis(120, 120, 120)
p.spilgtums()        # -> 120.0
p.ir_peleks()        # -> True
p.ir_tums()          # -> False

p2 = Pikselis(40, 30, 50)
p2.ir_peleks()       # -> False
p2.ir_tums()         # -> True
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

## 3. uzdevums — `Akumulators`

Telefona vai citas ierīces akumulators ar uzlādes pakāpi procentos.

**Atribūti:** `procenti` (sākotnējā uzlādes pakāpe no 0 līdz 100).

**Metodes:**

- `uzladet(p)` — palielina `procenti` par `p`. Ja iznāk vairāk par 100, paliek 100.
- `izladet(p)` — samazina `procenti` par `p`. Ja iznāk mazāk par 0, paliek 0.
- `ir_tukss()` — atgriež `True`, ja `procenti == 0`.
- `ir_pilns()` — atgriež `True`, ja `procenti == 100`.

**Piemēri:**

```python
a = Akumulators(50)
a.uzladet(30)
a.procenti          # -> 80

a.uzladet(50)
a.procenti          # -> 100
a.ir_pilns()        # -> True

a.izladet(150)
a.procenti          # -> 0
a.ir_tukss()        # -> True
```

---

## 4. uzdevums — `Auto`

Automašīna ar degvielas tvertni un nobraukumu.

**Atribūti:** `marka`, `degviela` (litri tvertnē), `paterins_100km` (degvielas patēriņš uz 100 km), `nobraukums` (sākumā 0).

**Metodes:**

- `brauk(km)` — pamēģina nobraukt `km` kilometrus.
  - Aprēķina vajadzīgo degvielu pēc formulas `km * paterins_100km / 100`.
  - Ja degvielas pietiek: samazina `degviela`, palielina `nobraukums` un atgriež `True`.
  - Ja nepietiek: neko nemaina un atgriež `False`.
- `uzpildit(litri)` — pievieno `litri` pie `degviela`.
- `tals_var_nobraukt()` — atgriež, cik kilometrus var nobraukt ar pašreizējo degvielu (`degviela * 100 / paterins_100km`).

**Piemēri:**

```python
a = Auto("Toyota", 40, 8)    # 8 litri uz 100 km
a.tals_var_nobraukt()        # -> 500.0

a.brauk(200)                 # -> True
a.degviela                   # -> 24.0
a.nobraukums                 # -> 200

a.brauk(400)                 # -> False (nepietiek degvielas)
a.uzpildit(20)
a.brauk(400)                 # -> True
a.degviela                   # -> 12.0
```

---

## 5. uzdevums — `Polinoms`

Polinoms ar koeficientiem (piem., `2 + x^2`).

**Atribūti:** `koef` (saraksts ar koeficientiem). `koef[0]` ir konstantes loceklis, `koef[1]` ir koeficients pie `x`, `koef[2]` ir koeficients pie `x^2`, utt.

**Metodes:**

- `vertiba(x)` — atgriež polinoma vērtību punktā `x`. Aprēķina kā `koef[0] + koef[1]*x + koef[2]*x^2 + ...`.
- `pakape()` — atgriež polinoma pakāpi (lielāko indeksu, kuram koeficients nav nulle). Ja visi koeficienti ir nulle, atgriež 0.
- `ir_lineara()` — atgriež `True`, ja polinoma pakāpe ir tieši 1.

**Piemēri:**

```python
p = Polinoms([2, 0, 1])    # 2 + 0*x + 1*x^2  =  2 + x^2
p.vertiba(3)               # -> 11
p.pakape()                 # -> 2
p.ir_lineara()             # -> False

p2 = Polinoms([5, 3])      # 5 + 3x
p2.vertiba(2)              # -> 11
p2.pakape()                # -> 1
p2.ir_lineara()            # -> True

p3 = Polinoms([0, 4, 0, 0])
p3.pakape()                # -> 1
p3.ir_lineara()            # -> True
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
