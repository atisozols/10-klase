# Pārbaudes darbs: Vārdnīcas — A variants

## 1. uzdevums — Kabineta meklēšana

Dota vārdnīca, kur atslēga ir mācību priekšmeta nosaukums, bet vērtība ir kabineta numurs.

Lietotājs ievada priekšmeta nosaukumu.

- Ja priekšmets ir vārdnīcā, izdrukā kabineta numuru.
- Ja nav, izdrukā `Nav datu`.

**Piemērs:**

```
Dota vārdnīca: {"Matematika": 214, "Biologija": 306, "Vesture": 112}
Ievade: "Biologija"
Izvade: 306
```

```
Dota vārdnīca: {"Matematika": 214, "Biologija": 306, "Vesture": 112}
Ievade: "Fizika"
Izvade: Nav datu
```

---

## 2. uzdevums — Preču daudzumu kopsavilkums

Dota vārdnīca, kur atslēga ir preces nosaukums, bet vērtība ir daudzums.

- Izdrukā kopējo preču skaitu vārdnīcā.
- Izdrukā visu daudzumu summu.

**Piemērs:**

```
Dota vārdnīca: {"maize": 4, "piens": 5, "siers": 2}
Izvade:
Preču skaits: 3
Kopā: 11
```

---

## 3. uzdevums — Vārdu pirmo burtu biežums

Lietotājs ievada teikumu.

- Sadalī teikumu vārdos.
- Izveido vārdnīcu, kas glabā katra vārda **pirmā burta** parādīšanās skaitu.
- Lielos un mazos burtus uzskati vienādi.
- Izdrukā katru burtu un tā skaitu formātā `<burts>: <skaits>`, saglabājot burtu pirmās parādīšanās secību.
- Beigās izdrukā visbiežāko pirmo burtu un tā skaitu. Ja ir vairāki vienādi, izdrukā pirmo no tiem.

**Piemērs:**

```
Ievade: "Anna lasa avenes ar Bruno"
Izvade:
a: 3
l: 1
b: 1
Visbiežākais: a (3)
```

---

## 4. uzdevums — Auksto pilsētu atlase

Dota vārdnīca, kur atslēga ir pilsētas nosaukums, bet vērtība ir temperatūra.

- Izveido jaunu vārdnīcu, kurā paliek tikai tās pilsētas, kur temperatūra ir mazāka par `0`.
- Izdrukā jauno vārdnīcu.
- Izdrukā, cik pilsētu tajā palika.
- Izdrukā šo temperatūru vidējo vērtību, noapaļotu līdz **1 zīmei** aiz komata.
- Ja nav nevienas pilsētas ar temperatūru zem `0`, izdrukā `Nav`.

**Piemērs:**

```
Dota vārdnīca: {"Riga": 3, "Aluksne": -5, "Madona": -2, "Liepaja": 1}
Izvade:
{"Aluksne": -5, "Madona": -2}
Pilsētas: 2
Vidējā: -3.5
```

---

## 5. uzdevums — Rezultātu izmaiņas

Dotas divas vārdnīcas `pirmais` un `otrais`, kur atslēga ir skolēna vārds, bet vērtība ir punktu skaits.

- Apskati tikai tos skolēnus, kuri ir **abās** vārdnīcās.
- Izveido jaunu vārdnīcu, kur:
  - atslēga ir skolēna vārds,
  - vērtība ir punktu izmaiņa `otrais - pirmais`.
- Izdrukā iegūto vārdnīcu.
- Izdrukā, cik skolēniem rezultāts ir uzlabojies.
- Izdrukā, cik skolēniem rezultāts ir pasliktinājies.
- Izdrukā, cik skolēniem rezultāts nav mainījies.

**Piemērs:**

```
pirmais = {"Anna": 7, "Juris": 5, "Liva": 9, "Bruno": 6}
otrais = {"Anna": 9, "Juris": 4, "Liva": 9, "Eva": 8}

Izvade:
{"Anna": 2, "Juris": -1, "Liva": 0}
Uzlabojās: 1
Pasliktinājās: 1
Bez izmaiņām: 1
```

---

## 6. uzdevums — Balsojuma rezultāti

Lietotājs cikliski ievada kandidāta vārdu.

- Ja ievadīta vērtība ir `stop`, ievadi beidz.
- Datus glabā vārdnīcā, kur:
  - atslēga ir kandidāta vārds,
  - vērtība ir saņemto balsu skaits.
- Ja kandidāts jau ir vārdnīcā, palielini viņa balsu skaitu par `1`.
- Beigās izdrukā katru kandidātu un viņa balsu skaitu formātā `<vārds>: <skaits>`, saglabājot kandidātu pirmās parādīšanās secību.
- Izdrukā kopējo balsu skaitu.
- Izdrukā uzvarētāju un viņa balsu skaitu. Ja vairākiem kandidātiem ir vienāds lielākais balsu skaits, izdrukā pirmo no tiem.
- Ja netika ievadīta neviena balss, izdrukā `Nav balsu`.

**Piemērs:**

```
Ievade:
"Anna"
"Juris"
"Anna"
"Liva"
"Anna"
"stop"

Izvade:
Anna: 3
Juris: 1
Liva: 1
Balsis: 5
Uzvarētājs: Anna (3)
```
