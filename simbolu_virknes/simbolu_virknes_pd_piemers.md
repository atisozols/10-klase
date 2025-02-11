# **Pārbaudes darbs: Simbolu virkņu apstrāde Python valodā**

**Darba ilgums:** 80 min  
**Maksimālais punktu skaits:** 100  

## **Norādījumi:**  
- Darbam atvēlētais laiks ir 80 minūtes.  
- Darbs sastāv no uzdevumiem, kuros jāanalizē kods, jāaizpilda tukšās vietas, jālabo kļūdas un jāraksta savs kods.  

---

## **1. Koda analīze (20 punkti)**  

Izlasiet kodu un atbildiet uz jautājumiem.

### **1.1** Kāda būs šī koda izvade? (5 punkti)  
```python
text = "abc123de45f6"
letters = ""
digits = ""

for char in text:
    if char.isalpha():
        letters += char
    else:
        digits += char

print(letters)
print(digits)
```
**Jūsu atbilde:**  

---

### **1.2** Ko dara šis kods? (5 punkti)  
```python
text = "pēteris"
new_text = ""

for i in range(len(text)):
    if i != 3:
        new_text += text[i]

print(new_text)
```
**Jūsu atbilde:**  

---

### **1.3** Kāds būs šī koda rezultāts? (5 punkti)  
```python
text = "Tukuma Raina Valsts gimnazija"
count = 0

for word in text.split():
    if word.istitle():
        count += 1

print(count)
```
**Jūsu atbilde:**  

---

### **1.4** Kas būs mainīgajā `t` pēc koda izpildes? (5 punkti)  
```python
text = "abc(de(fg)hij)kl(mn)op"
stavoklis = 0
t = ""

for char in text:
    if char == "(":
        stavoklis += 1
    elif char == ")":
        stavoklis -= 1
    elif stavoklis == 0:
        t += char

print(t)
```
**Jūsu atbilde:**  

---

## **2. Tukšo vietu aizpildīšana (20 punkti)**  

Aizpildiet trūkstošās vietas tā, lai kods strādātu pareizi.

### **2.1** Aizpildiet kodu, lai izvadītu vārdu skaitu tekstā. (5 punkti)  
```python
text = input("Ievadi teikumu: ")
print(__________)
```

---

### **2.2** Aizpildiet kodu, lai pārbaudītu, vai teksts ir palindroms (neņemot vērā atstarpes). (5 punkti)  
```python
text = input("Ievadi tekstu: ")
words = text.split()

t = ""
for w in words:
    t += w

t_reversed = ""
for i in range(len(t) - 1, ______, -1):
    t_reversed += t[i]

if t == t_reversed:
    print("ir palindroms")
else:
    print("nav")
```

---

### **2.3** Aizpildiet kodu, lai atrastu garāko vārdu teikumā. (5 punkti)  
```python
text = input("Ievadi teikumu: ")
words = text.split()

longest = words[0]
for word in words:
    if ________:
        longest = word

print(longest)
```

---

## **3. Kļūdu labošana (20 punkti)**  

### **3.1** Labojiet kļūdu, lai kods izvada tikai tos vārdus, kas beidzas ar “t”. (10 punkti)  
```python
sentence = "darīt vai nedarīt - tāds ir jautājums"
words = sentence.split()

for word in words:
    if word[_______] == "t":
        print(word)
```
➡ **Labojums:**  

---

## **4. Koda modificēšana (20 punkti)**  

### **4.1** Pārveidojiet kodu tā, lai tas pārbaudītu, vai divas virknes ir viena otras rotācijas versija. (10 punkti)  
```python
w1 = "tukums"
w2 = "kumstu"
found = False

for n in range(len(w1)):
    rotated = ""
    for i in range(n, len(w1)):
        rotated += w1[i]
    for i in range(0, n):
        rotated += w1[i]

    if ________:
        found = True
        break

print("Jā" if found else "Nē")
```

---

## **5. Papildu izaicinājums (10 punkti, bonuss)**  

Uzrakstiet Python programmu, kas **no teksta izvada visu, kas nav iekavās**.  
Piemērs:  
📌 `"abc(de(fg)hij)kl(mn)op"` → `"abcklop"`  

---

## **Vērtēšana:**  
- **85–100 punkti**: Izcili  
- **65–84 punkti**: Labi  
- **45–64 punkti**: Apmierinoši  
- **0–44 punkti**: Nepietiekami  

🔥 **Veiksmi!** 💻

