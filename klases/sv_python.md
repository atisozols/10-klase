### **1. uzdevums – Cilindra klase (volume un surface area)**

Izveido klasi `Cylinder`, kas saņem **radius** un **height**.
Izveido divas metodes:

- `volume()` – aprēķina tilpumu (`π * r² * h`)
- `surface_area()` – aprēķina virsmas laukumu (`2πr² + 2πrh`)

---

### **2. uzdevums – Grāmatu plaukts**

Izveido klasi `Book`, kurai ir lauki: `title`, `author`, `year`.
Izveido klasi `Bookshelf`, kas satur sarakstu ar grāmatām.
Pievieno metodes:

- `add_book(book)`
- `find_by_author(author)` – atgriež visas grāmatas, ko rakstījis konkrētais autors

---

### **3. uzdevums – Ledusskapis un produkti**

Izveido klasi `Product`, ar `name` un `quantity`.
Izveido klasi `Fridge`, kura satur sarakstu ar produktiem.
Pievieno metodes:

- `add_product(product)`
- `remove_product(name, amount)` – samazina daudzumu vai izņem produktu
- `list_contents()` – izvada visus produktus un daudzumus

---

### **4. uzdevums – Temperatūras pārveidotājs**

Izveido klasi `Temperature`, kurai ir atribūts `celsius`.
Izveido metodes:

- `to_fahrenheit()` – pārveido uz Fārenheita grādiem
- `to_kelvin()` – pārveido uz Kelviniem
- `describe()` – atgriež tekstu, piem.: `"25°C is 77°F or 298.15K"`

---

### **5. uzdevums – Punkti 3D telpā**

Izveido klasi `Point3D` ar koordinātēm `x`, `y`, `z`.
Izveido metodi `distance_to(other)`, kas aprēķina attālumu līdz citam 3D punktam.

---

### **6. uzdevums – Darbinieks un alga**

Izveido klasi `Employee` ar `name`, `hourly_rate` un `hours_worked`.
Izveido metodi `calculate_salary()` – kas aprēķina mēnešalgu (pieņemot 4 nedēļas mēnesī).
Pievieno metodi `give_raise(percent)`, kas palielina `hourly_rate` par procentiem.

---
