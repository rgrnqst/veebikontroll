# 🌐 Veebikontroll

Lihtne Python-programm, mis kontrollib, kas sisestatud veebileht töötab või on tõenäoliselt maas.

---

## ⚙️ Kuidas see töötab?

- Kasutaja sisestab veebiaadressi (näiteks `google.com`)
- Programm lisab automaatselt `https://` algusesse, kui vaja
- Kontrollib saidi olekut (kas vastab või mitte)
- Tagastab ühe kolmest vastusest:
  - ✅ **Töötab**
  - ⚠️ **Tõenäoliselt maas**
  - ❌ **Ei tööta või vigane link**

---

## 💻 Käivitamine (Pythoniga)

**Nõuded:**
- Python 3.10 või uuem
- `requests` moodul (`pip install requests`)

**Käivita käsurealt:**

```bash
python veebikontroll.py
