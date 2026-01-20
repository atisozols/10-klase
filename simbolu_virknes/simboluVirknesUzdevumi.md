# Python Strings – 10 uzdevumi (W3Schools pamati)

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
