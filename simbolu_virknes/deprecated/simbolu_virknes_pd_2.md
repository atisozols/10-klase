<p style="display: flex; justify-content: space-between;">
    <span>Vārds: _____________</span>
    <span>Datums: _____________</span>
</p>

### **Pārbaudes darbs: Simbolu virkņu apstrāde Python valodā**

**Variants:** 2  
**Darba ilgums:** 60 min  
**Maksimālais punktu skaits:** 45  

\fullhr

### Kāds uzdevums tiek risināts sekojošajā fragmentā? Dod vēl vienu `data` mainīgā piemēru un rezultātu! (5 punkti)  
```python
data = "abcfcbaacz"
tracker = ""

for symbol in data:
    if symbol in tracker:
        print(symbol)
        break
    tracker += symbol
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

### Kāds uzdevums tiek risināts sekojošajā fragmentā? Dod vēl vienu `data` mainīgā piemēru un rezultātu! (5 punkti)  
```python
data = "512301000"
pos = len(data) - 1

while pos >= 0 and data[pos] == "0":
    pos -= 1

data = data[:pos + 1]

print(data)
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

### Ko dara šis kods? Kas tiks izvadīts? (5 punkti)  
```python
data = "fly me to the moon"
chunks = data.split()

if len(chunks) > 0:
    measure = len(chunks[len(chunks) - 1])
    print(measure)
else:
    print(0)
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

\pagebreak

### Kāda būs šī koda izvade? Kādas simbolu virknes atšķir programma? Dod vienu piemēru, kad tiks izvadīts "Yes" un kad "No"? (5 punkti)  
```python
text = "abacbc"
seen = ""
for symbol in text:
    if symbol not in seen:
        seen += symbol

count_ref = text.count(seen[0])
valid = True

for symbol in seen:
    if text.count(symbol) != count_ref:
        valid = False
        break

if valid:
    print("Yes")
else:
    print("No")
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

### Kāds būs šī koda rezultāts? Kādas `text1` un `text2` vērtības iegūs pretēju rezultātu? (5 punkti)  
```python
text1 = "dog"
text2 = "cat"

if len(text1) != len(text2):
    print(False)
else:
    valid = True

    for symbol in text1:
        if text1.count(symbol) != text2.count(symbol):
            valid = False
            break

    print(valid)
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

\pagebreak

### Kas būs mainīgajā `t` pēc koda izpildes? Kas būtu jāpievieno, lai programma apstrādātu tikai simbolu virknes ar pareizi lietotām iekavām? (5 punkti)  
```python
text = "abc(de(fg(hi(jk(lm)no)p)qr)st)uv(wx)yz"
stavoklis = 0
t = ""

for char in text:
    if char == "(":
        stavoklis += 1
    elif char == ")":
        stavoklis -= 1
    elif stavoklis % 2 == 0:
        t += char

print(t)
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

### Ko izvadīs programma? (5 punkti)  
```python
data1 = "abcde"
data2 = "pqr"
result = ""

limit = min(len(data1), len(data2))

for j in range(limit):
    result += data1[j] + data2[j]

result += data1[limit:] + data2[limit:]

print(result)
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

\pagebreak

### Ko izvadīs programma? Kādam jābūt `data` mainīgajam, lai programma izvadītu pretēju rezultātu? (5 punkti)  
```python
text = "fivebigquackingzephyrsjoltmywaxbed"
pool = "abcdefghijklmnopqrstuvwxyz"
leftover = ""

for symbol in pool:
    if symbol not in text:
        leftover += symbol  

if leftover == "":
    print("Yes")
else:
    print("No")
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr

### Ko izvadīs programma? Kādam jābūt `text` mainīgajam, lai programma izvadītu `-1`? (5 punkti)  
```python
text = "bananagrapesorange"
pattern = "sora"

text_length = len(text)
pattern_length = len(pattern)
result = -1

for pos in range(text_length - pattern_length + 1):
    if text[pos:pos + pattern_length] == pattern:
        result = pos
        break

print(result)
```
**Atbilde:**  

<p>&nbsp;</p>
<p>&nbsp;</p>

\fullhr




