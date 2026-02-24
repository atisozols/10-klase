# Pārbaudes darbs: Simbolu virknes — B variants

**Darba ilgums:** 80 min  
**Maksimālais punktu skaits:** 100

---

## 1. uzdevums — Patskaņu noņemšana (10 punkti)

Lietotājs ievada tekstu.

- Izveido jaunu tekstu, kurā visi patskaņi (a, e, i, o, u — gan lielie, gan mazie) ir izņemti.
- Izdrukā jauno tekstu.
- Izdrukā, cik patskaņu tika izņemti.

**Piemērs:**

```
Ievade: "Hello World"
Izvade:
Hll Wrld
Izņemti: 3
```

```
Ievade: "AEIOUaeiou test"
Izvade:
 tst
Izņemti: 12
```

**Piezīme:** Patskaņu kopa ir `a, e, i, o, u` (tikai angļu valodas patskaņi).

---

## 2. uzdevums — Vārdu garumu analīze (12 punkti)

Lietotājs ievada teikumu (var būt liekas atstarpes sākumā un beigās).

- Attīri ievadi.
- Katram vārdam teikumā izdrukā vārdu un tā garumu formātā `<vārds>: <garums>`.
- Beigās izdrukā vidējo vārda garumu, noapaļotu līdz **1 zīmei** aiz komata.

**Piemērs:**

```
Ievade: " es esmu gudrs "
Izvade:
es: 2
esmu: 4
gudrs: 5
Vidējais garums: 3.7
```

---

## 3. uzdevums — Garākais "tīrais" vārds (15 punkti)

Lietotājs ievada tekstu.

- Sadalī tekstu vārdos.
- Atrodi **garāko** vārdu, kas satur **tikai burtus** (nevienu ciparu vai citu simbolu — katrs vārda simbols ir burts).
- Ja ir vairāki vienāda garuma, izdrukā **pirmo** no tiem.
- Ja neviens vārds nesatur tikai burtus, izdrukā `Nav`.

**Piemērs:**

```
Ievade: "abc 12xy hello3 world"
Izvade: world
```

```
Ievade: "a1b c2d 3e4"
Izvade: Nav
```

---

## 4. uzdevums — Laika validācija (18 punkti)

Lietotājs ievada laiku kā tekstu.

- Noņem liekās atstarpes sākumā un beigās.
- Pārbaudi, vai ievade atbilst formātam `HH:MM:SS`:
  - Kopējais garums ir tieši **8** simboli.
  - **3. un 6. simbols** (indeksi 2 un 5) ir kols `":"`.
  - Visi pārējie simboli ir **cipari**.
  - Stundas ir no **00** līdz **23**.
  - Minūtes ir no **00** līdz **59**.
  - Sekundes ir no **00** līdz **59**.
- Ja viss ir pareizi, izdrukā `Derīgs` un atsevišķi izdrukā stundas, minūtes un sekundes.
- Ja kaut kas nav pareizi, izdrukā `Nederīgs`.

**Piemērs:**

```
Ievade: "14:30:05"
Izvade:
Derīgs
Stundas: 14
Minūtes: 30
Sekundes: 05
```

```
Ievade: "25:61:00"
Izvade: Nederīgs
```

---

## 5. uzdevums — "Spēcīgo" vārdu meklēšana (20 punkti)

Lietotājs ievada tekstu.

- Sadalī tekstu vārdos.
- "Spēcīgs" vārds ir tāds, kas satur **vismaz vienu lielo burtu**, **vismaz vienu mazo burtu** UN **vismaz vienu ciparu**.
- Izdrukā visus "spēcīgos" vārdus (katru savā rindā).
- Beigās izdrukā kopējo "spēcīgo" vārdu skaitu.
- Ja tādu vārdu nav, izdrukā `Nav`.

**Piemērs:**

```
Ievade: "Hello abc Pass1word A1b test 123"
Izvade:
Pass1word
A1b
Spēcīgie vārdi: 2
```

```
Ievade: "hello WORLD 123"
Izvade: Nav
```

---

## 6. uzdevums — Apakšsecības pārbaude (25 punkti)

Lietotāji ievada divus tekstus (divas atsevišķas ievades).

- Pārbaudi, vai **otrais** teksts ir pirmā teksta **apakšsecība** (_subsequence_): vai otro tekstu var iegūt no pirmā, dzēšot dažus simbolus, bet **nemainot atlikušo simbolu secību**.
- Ja otrais teksts ir apakšsecība, izdrukā `YES` un izdrukā pirmo tekstu, **iezīmējot** katru atrastā simbola pozīciju ar lielo burtu (pārējos ar mazo). Sākotnēji pārveido visu pirmo tekstu uz mazajiem burtiem.
- Ja nav, izdrukā `NO`.

**Piemērs:**

```
Ievade 1: "programming"
Ievade 2: "pin"
Izvade:
YES
ProgrammINg
```

Skaidrojums: `p` atrodas pozīcijā 0, `i` — pozīcijā 8, `n` — pozīcijā 9. Šie simboli tiek izcelti ar lielajiem burtiem: `Programming` → `ProgrammINg` (p, i, n ir lielie).

Precīzāk:

```
p r o g r a m m i n g
P r o g r a m m I N g
```

Izvade: `ProgrammINg`

```
Ievade 1: "abcdef"
Ievade 2: "adf"
Izvade:
YES
AbcDeF
```

```
Ievade 1: "abcdef"
Ievade 2: "fa"
Izvade: NO
```

**Piezīme:** Salīdzināšana nav reģistrjūtīga — pirms apstrādes pārveido abus tekstus uz mazajiem burtiem.

---

**Vērtēšana:**

- **85–100 punkti** — Izcili
- **65–84 punkti** — Labi
- **45–64 punkti** — Apmierinoši
- **0–44 punkti** — Nepietiekami
