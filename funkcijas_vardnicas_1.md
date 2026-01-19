## **1. variants**

### **1. uzdevums**

```python
def add_one(x):
    return x + 1

def add_two(x):
    return x + 2

def increment(value):
    return add_one(value) + add_two(value)

result = increment(5)
print(result)
```

#### **Jautājumi**

1. Kas tiks izvadīts?
2. Kādu vērtību būtu nepieciešams padot `increment` funkcijai, lai programma izvadītu 17?

### **2. uzdevums**

```python
def search(arr):
    search_value = arr[0]
    for num in arr:
        if num > search_value:
            search_value = num
    return search_value

numbers = [3, 7, 2, 8, 4]
result = search(numbers)
print(result)
```

#### **Jautājumi**

1. Kas tiks izvadīts?
2. Dod sarakstu, ar kuru programma izvadīs 3!

### **3. uzdevums**

```python
data = {"x": 10, "Yz": 20, "z": 30}
for key in data:
    if key.islower():
        data[key] += 5
print(data)
```

#### **Jautājumi**

1. Kas tiks izvadīts?

### **1. variants - 4. uzdevums**

#### **Teorētiskie jautājumi:**

1. Vārdnīcas datu struktūra - nosauc tās īpašības, kā arī situācijas, kad vārdnīca ir piemērots risinājums.
2. Nosauc četras situācijas, kurās izmantot funkcijas ir vērtīga prakse. Pamato atbildi.
