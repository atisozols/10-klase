<p style="display: flex; justify-content: space-between;">
  <span>Vārds: _____________</span>
  <span>Datums: _____________</span>
</p>

### **Pārbaudes darbs: Pamata Python (izvade, ievade, nosacījumi, aritmētika)**

**Variants:** 2  
**Darba ilgums:** 60 min  
**Maksimālais punktu skaits:** 40  

\fullhr

### 1) Ko izvadīs? Paskaidro, ko salīdzina nosacījums. Kādam jābūt skaitlim, lai programma izdarītu vēlamo? (5 punkti)

```python
z = 407
if (z // 100) == (z % 10):
    print("OK")
else:
    print("NO")
```

**Atbilde / skaidrojums īsiem vārdiem:**

<p>&nbsp;</p>

\fullhr

### 2) Ko izvadīs? Kādu īpašību šis kods pārbauda? (5 punkti)

```python
p = 572
s = (p // 100) + ((p // 10) % 10) + (p % 10)
print(s % 2 == 0)
```

**Atbilde / skaidrojums:**

<p>&nbsp;</p>

\fullhr

### 3) Ko izvadīs? Paskaidro īsi, kā mainās mainīgais. (5 punkti)

```python
v = 132
print(v % 10)
v = v // 10
print(v % 10)
v = v // 10
print(v % 10)
```

**Atbilde / skaidrojums:**

<p>&nbsp;</p><p>&nbsp;</p>

\fullhr

### 4) Ko izvadīs? Ko varētu nozīmēt rezultāts? (5 punkti)

```python
t1 = 135
t2 = 45
print((t1 + t2) // 60, (t1 + t2) % 60)
```

**Atbilde:**

<p>&nbsp;</p>

\fullhr

### 5) Ko izvadīs? Kas mainīsies, ja mainīs `x`? (5 punkti)

```python
x = 137
a = x - (x % 10)
b = ((x // 10) * 10)
print(a, b, b - a)
```

**Atbilde / skaidrojums:**

<p>&nbsp;</p>

\fullhr

### 6) Ko izvadīs? Kādam skaitlim jābūt, lai iegūtu pretējo rezultātu? (5 punkti)

```python
m = 352
if (m // 100) + (m % 10) == (m // 10) % 10:
    print("X")
else:
    print("Y")
```

**Atbilde / skaidrojums:**

<p>&nbsp;</p>

\fullhr

### 7) Paskaidro, kas jāievada, lai iegūtu A un kas, lai iegūtu B. Kādiem jābūt ievadītajiem skaitļiem? (5 punkti)

```python
n = int(input("ievadi skaitli: "))
if (n % 2 == 0 and n % 3 == 0) or (n % 5 == 0):
    print("A")
else:
    print("B")
```

**Atbilde:**

<p>&nbsp;</p>

\fullhr

### 8) Ko izvadīs? Dod piemērus skaitļiem, kas iegūtu A, B un C. (5 punkti)

```python
a, b = int(input("ievadi pirmo skaitli: ")), int(input("ievadi otro skaitli: "))
if (a % 3) == (b % 3):
    print("A")
elif a > b:
    print("B")
else:
    print("C")
```

**Atbilde:**

<p>&nbsp;</p>