# Python vārdnīcas ceļvedis

Python vārdnīcas (dictionaries) ļauj saglabāt datus kā **atslēgu-vērtību** pārus. Ja jums jau ir pieredze ar masīviem/sarakstiem (lists), cikliem un virkņu (strings) apstrādi, šis ceļvedis palīdzēs jums ātri sākt darbu ar vārdnīcām!

---

## Kas ir Python vārdnīca?

- **Vārdnīca** ir kolekcija, kurā dati tiek glabāti kā atslēgu un vērtību pāri.
- Katram pārim ir **atslēga** (key) un **vērtība** (value). Atslēgas parasti ir unikālas.
- Vārdnīcas tiek definētas, izmantojot figūriekavas `{}`.

---

```python
# Vienkārša vārdnīca
students = {
    "Anna": 17,
    "Jānis": 18,
    "Līga": 16
}
print(students)
```

---

## Piekļuve un Modificēšana

### Piekļuve vērtībai

Lai piekļūtu kādas atslēgas vērtībai, izmantojiet kvadrātiekavas `[]`.

```python
print(students["Anna"])  # Izdrukās: 17
```

### Jaunu elementu pievienošana

Vienkārši piešķiriet vērtību jaunai atslēgai.

```python
students["Pēteris"] = 17
print(students)
```

### Elementa modifikācija

Lai mainītu esošas atslēgas vērtību, piešķiriet jaunu vērtību.

```python
students["Anna"] = 18
print(students)
```

### Atslēgas dzēšana

Lai dzēstu atslēgu, izmantojiet `del` operatoru.

```python
del students["Līga"]
print(students)
```

---

## Iterēšana cauri vārdnīcai

Lai apstrādātu katru atslēgu un vērtību vārdnīcā, izmantojiet `for` cilpu.

```python
for key, value in students.items():
    print(f"{key} ir {value} gadus vecs")
```

---

## Papildu funkcijas un metodes

- **`keys()`** – atgriež visas atslēgas.
- **`values()`** – atgriež visas vērtības.
- **`items()`** – atgriež atslēgu-vērtību pārus.
- **`get(key, default)`** – atgriež vērtību, ja atslēga pastāv; pretējā gadījumā atgriež noklusējuma vērtību.

```python
# Piemērs ar get() metodi
print(students.get("Zane", "Nav atrasts"))
```

## Uzdevumi
### 1. Uzdevums: Vienkārša vārdnīcas izveide
**Uzdevums:** Izveido vārdnīcu ar vismaz trim atslēgu-vērtību pāriem, kur atslēgas ir jūsu mīļāko sporta veidu nosaukumi, un vērtības – spēlētāju skaits (izdomājiet vērtības). Izdrukājiet vārdnīcu.
### 2. Uzdevums: Elementu pievienošana un dzēšana
**Uzdevums:** Pievieno pie iepriekš izveidotās vārdnīcas jaunu pāri (piemēram, "Basketbols": 5). Pēc tam dzēs pāri, kura atslēga ir kāds no iepriekšējiem elementiem. Izdrukājiet gala vārdnīcu.
### 3. Uzdevums: Vārdnīcas cikliska apstrāde
**Uzdevums:** Izveido programmu, kas cikliski apstrādā vārdnīcu un izdrukā katru atslēgu un tās vērtību formātā:  
`"Sporta veids: <atslēga>, Spēlētāju skaits: <vērtība>"`.
### 4. Uzdevums: Vērtību modifikācija
**Uzdevums:** Modificē vārdnīcā esošu sporta veidu vērtību, palielinot katra sporta veida spēlētāju skaitu par 1. Izdrukājiet atjaunināto vārdnīcu.
### 5. Uzdevums: Funkcija, kas filtrē vārdnīcu
**Uzdevums:** Izveido funkciju `filtrēt_sportus(vardnica)`, kas saņem kā argumentu vārdnīcu un atgriež jaunu vārdnīcu, kurā iekļauti tikai tie sporta veidi, kuru spēlētāju skaits ir lielāks par 5. Pārbaudiet funkciju ar savu vārdnīcu un izdrukājiet rezultātu.
