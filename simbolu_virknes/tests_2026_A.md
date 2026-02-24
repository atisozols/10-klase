# Pārbaudes darbs: Simbolu virknes — A variants

**Darba ilgums:** 80 min  
**Maksimālais punktu skaits:** 100

---

## 1. uzdevums — Ciparu maskēšana (10 punkti)

Lietotājs ievada tekstu.

- Izveido jaunu tekstu, kurā katrs cipars ir aizstāts ar simbolu `#`.
- Izdrukā jauno tekstu.
- Izdrukā, cik ciparu tika aizstāti.

**Piemērs:**

```
Ievade: "Mans telefons ir 291-456-78"
Izvade:
Mans telefons ir ###-###-##
Aizstāti: 8
```

---

## 2. uzdevums — Vārdu secības apgriešana (12 punkti)

Lietotājs ievada teikumu (var būt liekas atstarpes sākumā un beigās).

- Attīri ievadi (noņem atstarpes sākumā un beigās).
- Izdrukā teikumu, kurā vārdu secība ir apgriezta, bet paši vārdi paliek nemainīti.

**Piemērs:**

```
Ievade: " šodien ir laba diena "
Izvade: diena laba ir šodien
```

---

## 3. uzdevums — Populārākais simbols (15 punkti)

Lietotājs ievada tekstu.

- Atrodi simbolu, kas parādās tekstā visbiežāk (**neskaitot atstarpes**).
- Ja vairākiem simboliem ir vienāds biežums, izdrukā to, kas pirmais parādās tekstā.
- Izdrukā šo simbolu un cik reizes tas parādās.

**Piemērs:**

```
Ievade: "abracadabra"
Izvade:
Simbols: a
Skaits: 5
```

```
Ievade: "aabb"
Izvade:
Simbols: a
Skaits: 2
```

---

## 4. uzdevums — Datuma validācija (18 punkti)

Lietotājs ievada datumu kā tekstu.

- Noņem liekās atstarpes sākumā un beigās.
- Pārbaudi, vai ievade atbilst formātam `DD.MM.GGGG`:
  - Kopējais garums ir tieši **10** simboli.
  - **3. un 6. simbols** (indeksi 2 un 5) ir punkts `"."`.
  - Visi pārējie simboli ir **cipari**.
  - Diena ir no **01** līdz **31**.
  - Mēnesis ir no **01** līdz **12**.
- Ja viss ir pareizi, izdrukā `Derīgs` un atsevišķi izdrukā dienu, mēnesi un gadu.
- Ja kaut kas nav pareizi, izdrukā `Nederīgs`.

**Piemērs:**

```
Ievade: "25.12.2025"
Izvade:
Derīgs
Diena: 25
Mēnesis: 12
Gads: 2025
```

```
Ievade: "32.13.2025"
Izvade: Nederīgs
```

---

## 5. uzdevums — Patskaņu šifrs (20 punkti)

Lietotājs ievada tekstu.

- Izveido šifrētu tekstu pēc šādas loģikas:
  - Katru patskaņi aizstāj ar **nākamo** patskaņi ciklā: `a→e`, `e→i`, `i→o`, `o→u`, `u→a`.
  - Ja burts ir **lielais**, rezultātam arī jābūt lielajam burtam: `A→E`, `E→I`, `I→O`, `O→U`, `U→A`.
  - Visus pārējos simbolus (līdzskaņus, ciparus, atstarpes, pieturzīmes) atstāj **nemainītus**.
- Izdrukā šifrēto tekstu.

**Piemērs:**

```
Ievade: "Atis ir OK"
Izvade: Etos or UK
```

```
Ievade: "ubuntu"
Izvade: abantu
```

**Piezīme:** Patskaņu kopa ir `a, e, i, o, u` (tikai angļu valodas patskaņi).

---

## 6. uzdevums — Vārdu kompresija (25 punkti)

Lietotājs ievada teikumu.

- Attīri ievadi.
- Sadalī teikumu vārdos.
- Saspiež secīgi atkārtojošos **vārdus**: katru grupu vienādu secīgu vārdu aizstāj ar `<vārds><skaits>`.
- Izdrukā saspiesto rezultātu (elementus atdalot ar atstarpēm).
- Izdrukā kopējo grupu skaitu.
- Izdrukā lielākās grupas izmēru un vārdu, kuram tā pieder (ja vairākas vienādas — pirmo).

**Piemērs:**

```
Ievade: "labi labi labi slikti slikti labi"
Izvade:
labi3 slikti2 labi1
Grupas: 3
Lielākā grupa: labi (3)
```

```
Ievade: "es es es es"
Izvade:
es4
Grupas: 1
Lielākā grupa: es (4)
```

---

**Vērtēšana:**

- **85–100 punkti** — Izcili
- **65–84 punkti** — Labi
- **45–64 punkti** — Apmierinoši
- **0–44 punkti** — Nepietiekami
