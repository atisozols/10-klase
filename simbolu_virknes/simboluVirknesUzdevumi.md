# Python Strings – 16 uzdevumi (W3Schools pamati)

## 1. Indeksēšana

Dots:

```python
s = "Programming"
```

Uzdevumi:

- Izdrukā pirmo simbolu.
- Izdrukā pēdējo simbolu.
- Izdrukā 4. simbolu.
- Izdrukā priekšpēdējo simbolu.

## 2. Sagriešana (slicing)

Dots:

```python
s = "DataStructures"
```

Uzdevumi:

- Izdrukā pirmos 4 simbolus.
- Izdrukā pēdējos 5 simbolus.
- Izdrukā visu, izņemot pirmo simbolu.
- Izdrukā katru otro simbolu (izmantojot slicing principu).

## 3. Garums + pārbaude

Uzraksti programmu, kas prasa lietotājam ievadīt lietotājvārdu (tekstu).

- Ja len(username) < 4, izdrukā: "Too short".
- Ja len(username) > 12, izdrukā: "Too long".
- Pretējā gadījumā izdrukā: "OK".

## 4. Piederības pārbaude (in)

Uzraksti programmu:

```python
email = input("Enter email: ")
```

Uzdevumi:

- Pārbaudi, vai e-pastā ir gan "@", gan ".".
- Izdrukā "Looks valid" tikai tad, ja ir abi; citādi izdrukā "Invalid".

## 5. Simbolu skaitīšana bez .count()

Dots:

```python
text = input("Enter text: ")
target = input("Enter a character to count: ")
```

Uzdevums:

- Saskaiti, cik reizes target parādās text, izmantojot ciklu un indeksēšanu (neizmanto .count()).
- Izdrukā iegūto skaitu.

## 6. Ievades “attīrīšana”: strip() + formatēšana

Prasi lietotājam ievadīt vārdu un uzvārdu (var būt liekas atstarpes).

- Izmanto .strip(), lai noņemtu atstarpes sākumā un beigās.
- Izdrukā pilno vārdu formātā: "Uzvārds, Vārds".

## 7. Burtu reģistra normalizēšana (lower() / upper())

Uzraksti programmu:

```python
answer = input("Do you agree? (yes/no): ")
```

Uzdevumi:

- Pieņem ievades kā "YES", "Yes", " yes " kā “yes”.
- Normalizē ievadi (strip + lower) un izlem, vai tā ir “yes” vai “no”.
- Izdrukā "Accepted" (yes), "Rejected" (no), citādi "Unknown input".

## 8. Aizliegto vārdu aizstāšana (replace())

Dots:

```python
text = input("Write a comment: ")
```

Uzdevums:

- Aizstāj visas "bad" parādīšanās reizes ar "\*\*\*" (var būt case-sensitive).
- Izdrukā “cenzēto” komentāru.

## 9. Vārdu sadalīšana un analīze (split())

Prasi lietotājam ievadīt teikumu.

- Sadalī to vārdos.
- Izdrukā:
  - vārdu skaitu,
  - pirmo vārdu,
  - garāko vārdu (ja ir vairāki vienādi garākie, izdrukā pirmo no tiem).

## 10. Teksta formatēšana (f-strings / format())

Doti ievades dati:

```python
product = input("Product name: ")
price = float(input("Price: "))
qty = int(input("Quantity: "))
```

Uzdevums:

- Aprēķini total = price \* qty.
- Izdrukā “čeku” vienā rindā, piemēram:
  - "3 x Apple at 0.50 EUR = 1.50 EUR"
- Nodrošini, ka naudas vērtības tiek rādītas ar 2 zīmēm aiz komata.

## 11. Apakšvirknes meklēšana (find() / rfind())

Uzraksti programmu:

```python
text = input("Enter text: ")
keyword = input("Enter keyword: ")
```

Uzdevumi:

- Atrodi un izdrukā keyword pirmo parādīšanās indeksu (izmanto .find()).
- Atrodi un izdrukā keyword pēdējo parādīšanās indeksu (izmanto .rfind()).
- Ja keyword parādās vismaz 2 reizes, izdrukā teksta daļu, kas atrodas starp pirmo un pēdējo keyword parādīšanos (neiekļaujot pašu keyword).

## 12. Paroles pārbaude (vairāki nosacījumi)

Prasi lietotājam ievadīt paroli.

Izdrukā "Strong" tikai tad, ja izpildās visi nosacījumi:

- Paroles garums ir vismaz 8.
- Parolē ir vismaz viens cipars.
- Parolē ir vismaz viens lielais burts.
- Parolē nav atstarpju.

Ja kaut kas neizpildās, izdrukā "Weak" un pēc tam izdrukā katru neizpildīto nosacījumu atsevišķā rindā.

## 13. Akronīms no teikuma (split() + indeksēšana)

Prasi lietotājam ievadīt frāzi (var būt liekas atstarpes, piemēram: " Central Processing Unit ").

Uzdevumi:

- Attīri ievadi (strip).
- Sadalī frāzi vārdos.
- Izveido akronīmu no katra vārda pirmā burta.
- Izdrukā akronīmu ar lielajiem burtiem.

## 14. Raksta atpazīšana: atkārtots fragments

Prasi lietotājam ievadīt virkni s.

Uzdevums:

- Nosaki, vai s var iegūt, atkārtojot kādu īsāku, netukšu fragmentu vairāk nekā 1 reizi (piemēram, "abcabcabc" vai "aaaa").
- Ja var, izdrukā "YES" un īsāko fragmentu, kuru atkārtojot iegūst s.
- Ja nevar, izdrukā "NO".

## 15. Palindroms (normalizēšana + pārbaude)

Prasi lietotājam ievadīt tekstu.

Uzdevumi:

- Pārvērt tekstu uz mazajiem burtiem.
- Izmet ārā visas rakstzīmes, kas nav burti vai cipari.
- Pārbaudi, vai rezultāts ir palindroms (lasa vienādi no abām pusēm).
- Izdrukā "Palindrome" vai "Not palindrome".

## 16. Garākā distance starp nullēm (0/1 virkne)

Dots:

```python
sv = input("Enter 0/1 string: ")
```

Uzdevums:

- Dota simbolu virkne, kas sastāv tikai no "0" un "1".
- Atrodi garāko distanci starp divām nullēm (t.i., lielāko "1" simbolu skaitu starp divām "0").
- Ja virknē nav vismaz 2 nulles, izdrukā 0.
