# Pārbaudes darbs: Simbolu virknes — C variants

---

## 1. uzdevums — Ciparu izņemšana (10 punkti)

Lietotājs ievada tekstu.

- Izveido jaunu tekstu, kurā visi cipari ir izņemti.
- Izdrukā jauno tekstu.
- Izdrukā, cik ciparu tika izņemti.

**Piemērs:**

```
Ievade: "abc12de405"
Izvade:
abcde
Izņemti: 5
```

---

## 2. uzdevums — Vārdu analīze (12 punkti)

Lietotājs ievada teikumu (var būt liekas atstarpes sākumā un beigās).

- Attīri ievadi.
- Sadalī teikumu vārdos.
- Izdrukā vārdu skaitu.
- Izdrukā pirmo vārdu.
- Izdrukā pēdējo vārdu.
- Izdrukā garāko vārdu. Ja ir vairāki vienāda garuma vārdi, izdrukā pirmo no tiem.

**Piemērs:**

```
Ievade: " šodien būs ļoti jauka diena "
Izvade:
Vārdi: 5
Pirmais: šodien
Pēdējais: diena
Garākais: šodien
```

**Piezīme:** Vari pieņemt, ka pēc attīrīšanas ievadē ir vismaz viens vārds.

---

## 3. uzdevums — Pirmais neatkārtojošais simbols (15 punkti)

Lietotājs ievada tekstu.

- Atrodi pirmo simbolu, kas tekstā parādās tieši **1 reizi**.
- Atstarpes neņem vērā.
- Ja tāda simbola nav, izdrukā `Nav`.

**Piemērs:**

```
Ievade: "aabbcdde"
Izvade: c
```

```
Ievade: "anna"
Izvade: Nav
```

---

## 4. uzdevums — Koda validācija (18 punkti)

Lietotājs ievada kodu kā tekstu.

- Noņem liekās atstarpes sākumā un beigās.
- Pārbaudi, vai ievade atbilst formātam `LLL-DDD`:
  - kopējais garums ir tieši **7** simboli,
  - **4. simbols** (indekss 3) ir defise `-`,
  - pirmie **3** simboli ir burti,
  - pēdējie **3** simboli ir cipari.
- Ja viss ir pareizi, izdrukā `Derīgs` un atsevišķi izdrukā burtu daļu ar lielajiem burtiem un ciparu daļu.
- Ja kaut kas nav pareizi, izdrukā `Nederīgs`.

**Piemērs:**

```
Ievade: "abc-123"
Izvade:
Derīgs
Burti: ABC
Cipari: 123
```

```
Ievade: "ab-1234"
Izvade: Nederīgs
```

---

## 5. uzdevums — Burti un cipari atsevišķi (20 punkti)

Lietotājs ievada tekstu.

- Izveido 2 jaunas virknes:
  - vienu tikai no burtiem,
  - otru tikai no cipariem.
- Saglabā simbolu sākotnējo secību.
- Izdrukā abas virknes katru savā rindā.
- Izdrukā, cik citu simbolu (ne burtu un ne ciparu) bija tekstā.

**Piemērs:**

```
Ievade: "ab-12 cd!34"
Izvade:
Burti: abcd
Cipari: 1234
Citi simboli: 3
```

---

## 6. uzdevums — Simbolu kompresija (25 punkti)

Lietotājs ievada tekstu.

- Attīri ievadi.
- Izveido jaunu virkni, kurā secīgi vienādie simboli tiek saspiesti šādi: katru vienādo simbolu grupu aizvieto ar `<simbols><skaits>`.
- Izdrukā saspiesto virkni.
- Izdrukā kopējo grupu skaitu.
- Izdrukā lielākās grupas garumu un simbolu, kuram tā pieder. Ja ir vairākas vienādas lielākās grupas, izdrukā pirmo.

**Piemērs:**

```
Ievade: "aaabbcaaa"
Izvade:
a3b2c1a3
Grupas: 4
Lielākā grupa: a (3)
```

```
Ievade: "xxxx"
Izvade:
x4
Grupas: 1
Lielākā grupa: x (4)
```
