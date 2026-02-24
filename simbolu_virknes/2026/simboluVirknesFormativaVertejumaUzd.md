# Simbolu virknes — formatīvais vērtējums (2 uzdevumi)

## 1. Krāsu koda validācija (#RRGGBB)

Uzraksti programmu:

```python
color = input("Ievadi krāsu kodu: ")
```

Uzdevumi:

- Noņem liekās atstarpes ievades sākumā un beigās.
- Pārbaudi, vai ievade atbilst formātam `#RRGGBB`:
  - pirmais simbols ir `#`,
  - garums ir tieši 7,
  - pārējie 6 simboli ir tikai no kopas `0–9` vai `A–F` (atļauj arī mazos burtus).
- Ja ievade ir korekta, izdrukā:
  - `Valid`
  - normalizētu kodu ar lielajiem burtiem (piemēram, `#1A2B3C`)
  - atsevišķi arī `RR`, `GG`, `BB` daļas (kā teksta gabalus).
- Ja ievade nav korekta, izdrukā `Invalid`.

## 2. Simbolu virknes kompresija (cikliski jāapstrādā virkne)

Uzraksti programmu:

```python
s = input("Ievadi tekstu: ")
```

Uzdevumi:

- Noņem liekās atstarpes ievades sākumā un beigās.
- Izveido jaunu virkni, kurā secīgi vienādie simboli tiek “saspiesti” šādi: katru vienādo simbolu grupu aizvieto ar `<simbols><skaits>`.
  - Piemērs: `aaabbcaaa` -> `a3b2c1a3`
- Izdrukā saspiesto virkni.
- Izdrukā, cik grupas kopā bija.
- Izdrukā lielāko grupas garumu un simbolu, kuram šis garums bija (ja ir vairākas vienādas, pietiek ar pirmo).
