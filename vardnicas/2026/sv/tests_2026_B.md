# Pārbaudes darbs: Vārdnīcas — B variants

## 1. uzdevums — Telefongrāmatas atjaunošana

Dota vārdnīca, kur atslēga ir cilvēka vārds, bet vērtība ir tālruņa numurs.

Lietotājs ievada vārdu un tālruņa numuru.

- Pievieno šo pāri vārdnīcai, ja tāda vārda vēl nav.
- Ja tāds vārds jau ir vārdnīcā, nomaini veco numuru ar jauno.
- Izdrukā saglabāto numuru šim vārdam.
- Izdrukā kopējo kontaktu skaitu vārdnīcā.

**Piemērs:**

```
Dota vārdnīca: {"Anna": "20010010", "Juris": "25554444"}
Ievade:
Vārds: "Anna"
Numurs: "29998888"

Izvade:
Anna: 29998888
Kontakti: 2
```

```
Dota vārdnīca: {"Anna": "20010010", "Juris": "25554444"}
Ievade:
Vārds: "Liva"
Numurs: "26667777"

Izvade:
Liva: 26667777
Kontakti: 3
```

---

## 2. uzdevums — Atzīmju sadalījums

Lietotājs ievada atzīmes vienā rindā, atdalītas ar atstarpēm.

- Izveido vārdnīcu, kas glabā katras atzīmes parādīšanās skaitu.
- Izdrukā katru atzīmi un tās biežumu formātā `<atzīme>: <skaits>`, saglabājot atzīmju pirmās parādīšanās secību.
- Beigās izdrukā dažādo atzīmju skaitu.
- Izdrukā visbiežāko atzīmi un tās skaitu. Ja ir vairākas vienādas, izdrukā pirmo no tām.

**Piemērs:**

```
Ievade: "8 10 8 7 10 8"
Izvade:
8: 3
10: 2
7: 1
Dažādas atzīmes: 3
Visbiežākā: 8 (3)
```

---

## 3. uzdevums — Rezervāciju atcelšana

Dota vārdnīca, kur atslēga ir rezervācijas kods, bet vērtība ir rezervēto vietu skaits.

Lietotājs ievada rezervāciju kodus vienā rindā, atdalītus ar atstarpēm.

- Katram ievadītajam kodam:
  - ja kods ir vārdnīcā, dzēs to no vārdnīcas,
  - ja nav, ignorē to.
- Izdrukā atjaunoto vārdnīcu.
- Izdrukā, cik rezervācijas tika dzēstas.
- Izdrukā, cik vietu kopā tika atbrīvots.

**Piemērs:**

```
Dota vārdnīca: {"A12": 3, "B07": 2, "C99": 5, "D10": 1}
Ievade: "B07 X11 C99"

Izvade:
{"A12": 3, "D10": 1}
Dzēstas: 2
Atbrīvotas vietas: 7
```

---

## 4. uzdevums — Punktu līmeņi

Dota vārdnīca, kur atslēga ir skolēna vārds, bet vērtība ir punktu skaits.

- Izveido jaunu vārdnīcu ar trim atslēgām:
  - `bronza`, ja punktu skaits ir mazāks par `50`,
  - `sudrabs`, ja punktu skaits ir no `50` līdz `79`,
  - `zelts`, ja punktu skaits ir vismaz `80`.
- Jaunās vārdnīcas vērtība ir skolēnu skaits katrā līmenī.
- Izdrukā jauno vārdnīcu.
- Izdrukā, kurā līmenī ir visvairāk skolēnu. Ja vairākos līmeņos skaits ir vienāds, izdrukā pirmo no tiem.

**Piemērs:**

```
Dota vārdnīca: {"Anna": 42, "Juris": 80, "Liva": 75, "Bruno": 91, "Eva": 60}
Izvade:
{"bronza": 1, "sudrabs": 2, "zelts": 2}
Lielākais līmenis: sudrabs (2)
```

---

## 5. uzdevums — Anagrammu pārbaude

Lietotājs ievada divus tekstus.

- Pārvērt abus tekstus uz mazajiem burtiem.
- Ignorē atstarpes.
- Izmantojot vārdnīcas, pārbaudi, vai abos tekstos ir vienāds katra burta skaits.
- Ja teksti ir anagrammas, izdrukā `Jā`.
- Ja nav, izdrukā `Nē`.

**Piemērs:**

```
Ievade 1: "Suns"
Ievade 2: "suns"
Izvade: Jā
```

```
Ievade 1: "laiva"
Ievade 2: "viela"
Izvade: Nē
```

---

## 6. uzdevums — Iepirkumu grozs

Lietotājs cikliski ievada preces nosaukumu.

- Ja ievadīta vērtība ir `stop`, ievadi beidz.
- Pretējā gadījumā lietotājs ievada šīs preces cenu.
- Datus glabā vārdnīcā, kur:
  - atslēga ir preces nosaukums,
  - vērtība ir šīs preces kopējā cena grozā.
- Ja prece jau ir vārdnīcā, pieskaiti jauno cenu pie esošās vērtības.
- Beigās izdrukā katru preci un tās kopējo cenu formātā `<prece>: <summa>`.
- Izdrukā groza kopējo summu.
- Izdrukā preci ar lielāko kopējo cenu. Ja ir vairākas vienādas, izdrukā pirmo atrasto.
- Ja netika ievadīta neviena prece, izdrukā `Grozs tukšs`.

**Piemērs:**

```
Ievade:
Prece: "piens"
Cena: 1.20
Prece: "maize"
Cena: 1.50
Prece: "piens"
Cena: 0.80
Prece: "stop"

Izvade:
piens: 2.00
maize: 1.50
Kopā: 3.50
Lielākā summa: piens (2.00)
```
