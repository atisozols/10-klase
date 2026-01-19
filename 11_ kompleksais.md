# 11. klases kombinētais pārbaudes darbs – Programmēšana (80 minūtes)

**Atceries! (20 punkti)**
Katrs uzdevums – 5 punkti

1. Nosauc trīs HTML elementus, kurus izmanto satura strukturēšanai.

2. Uzraksti SQL komandu, kas izveido tabulu `books` ar kolonnām `id`, `title`, `author`.

3. Kas ir `GET` pieprasījums tīmekļa lietotnē, un ko tas dara?

4. Kāda ir atšķirība starp `div` un `span` HTML elementiem?

---

**Lieto zināšanas pazīstamās situācijās (50 punkti)**

5. Uzraksti SQL vaicājumu, kas atlasa visus lietotājus no tabulas `users`, kuru vecums ir lielāks par 18.

6. Izveido HTML formu ar diviem laukiem – `vārds` un `e-pasts` – kas sūta datus uz `/submit` ar `POST` metodi.

7. Uzraksti JavaScript funkciju, kas pārbauda, vai ievadītais skaitlis ir pāra vai nepāra skaitlis.

8. Uzraksti Express servera `POST` maršrutu `/submit`, kas saņem vārdu un e-pastu un izvada tos konsolē.

9. Izveido vienkāršu React komponenti `UserCard`, kas attēlo komponentei padotus `name` un `email`.

---

**Lieto zināšanas jaunās situācijās, skaidro, labo (25 punkti)**

10. **(10 punkti)** Šis SQL vaicājums nestrādā. Atrodi un paskaidro vismaz 2 kļūdas:

```sql
SELECT name email FROM users WHERE age => 18;
```

11. **(15 punkti)** Apskati zemāk doto React komponenti. Atrodi un izskaidro kļūdas, piedāvā labojumus:

```jsx
function Welcome(props) {
  const [name, setName] = "";
  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <p>Hello, {props.name}!</p>
    </div>
  );
}
```

---

12. Apraksti tīmekļa lietotnes struktūru, kas:

- Parāda reģistrācijas formu.
- Validē reģistrācijas datus.
- Ļauj datus iesniegt.
- Katrs iesniegums tiek saglabāts.

---
