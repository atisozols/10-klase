## **2. variants**

### **1. uzdevums**

```python
def double(x):
    return x * 2

def triple(x):
    return x * 3

def transform(value):
    return double(value) + triple(value)

output = transform(4)
print(output)
```

#### **Questions:**

1. Kas tiks izvadīts?
2. Kādu vērtību būtu nepieciešams padot `transform` funkcijai, lai programma izvadītu 35?

### **2. uzdevums**

```python
def rakete(s):
    result = ""
    for char in s:
        result = char + result
    return result

text = "Python"
result = rakete(text)
print(result)
```

#### **Jautājumi**

1. Kas tiks izvadīts?
2. Ko jāpadod programmai, lai tā izvadītu "Anna"?

### **3. uzdevums**

```python
data = {"x": 10, "yz": 20, "z": 30}
for key in data:
    if len(key) > 1:
        data[key] += 5
data["c"] = 3
print(data)
```

#### **Jautājumi**

1. Kas tiks izvadīts?

### **4. uzdevums**

#### **Teorētiskie jautājumi:**

1. Vārdnīcas datu struktūra - nosauc tās īpašības, kā arī situācijas, kad vārdnīca ir piemērots risinājums.
2. Nosauc četras situācijas, kurās izmantot funkcijas ir vērtīga prakse. Pamato atbildi.
