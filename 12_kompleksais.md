# 12. klases kombinētais pārbaudes darbs – Programmēšana (80 minūtes)

**Atceries! (20 punkti)**
Katrs uzdevums – 5 punkti

1. Nosauc trīs atšķirības starp melnās kastes un baltās kastes testēšanu.

2. Kas ir steks un kā tas darbojas (norādi galveno darbību nosaukumus)?

3. Uzraksti vienkāršu SQL komandu, kas izdzēš tabulu `students` no datubāzes.

4. Kas ir programmatūras prasību specifikācija un kādam nolūkam to izmanto?

**Lieto zināšanas zināmās situācijās (50 punkti)**
Katrs uzdevums – 10 punkti

5. Uzraksti Python funkciju, kas pieņem sarakstu un atgriež jaunu sarakstu ar tikai tiem skaitļiem, kas ir lielāki par vidējo.

6. Definē vienkāršu `LinkedListNode` klasi Python, kur katram mezglam ir `value` un `next` atribūti.

7. Izveido UML klases diagrammu sistēmai, kurā ir `User`, `AdminUser`, un `Post` klases ar attiecībām.

8. Uzraksti kodu, kas simulē rindu (queue) izmantojot Python sarakstu metodes.

9. Aizpildi tabulu ar pareizu testēšanas metodes veidu:

| Testa veids        | Apraksts                               |
| ------------------ | -------------------------------------- |
| Vienībtestēšana    | Testē atsevišķas funkcijas vai metodes |
| Integrācijas tests | ?                                      |
| Akcepttests        | ?                                      |
| Melnā kaste        | ?                                      |
| Baltā kaste        | ?                                      |

**Skaidro, salīzini, analizē. (25 punkti)**

10. **(10 punkti)** Apraksti atšķirības starp ūdens krituma modeli (Waterfall) un elastīgajiem izstrādes modeļiem (piemēram, Agile). Mini vismaz 3 salīdzinājumus.

11. **(15 punkti)** Dotais Python kods izmanto bināro koku. Apraksti, kā darbojas `insert` metode un kādēļ koks ir noderīgs datu glabāšanai.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = Node(new_value)
            else:
                self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = Node(new_value)
            else:
                self.right.insert(new_value)
```

**Komplekss problēmas risinājums/vispārinājums. (5 punkti)**

12. **(5 punkti)** Tev ir uzdevums izstrādāt jaunu tīmekļa lietotni. Apraksti 3 veida izpētes metodes, ko izmantotu, lai noskaidrotu mērķauditorijas vajadzības. Paskaidro, kā kāda no vajadzībām varētu ietekmēt tava produkta dizainu.
