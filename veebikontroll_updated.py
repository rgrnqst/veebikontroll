import requests


def värvitud_tulemus(tekst, tüüp):
    värvid = {
        "ok": "\033[92m",       
        "hoiatus": "\033[93m",  
        "viga": "\033[91m",     
        "lõpp": "\033[0m"       
    }
    return f"{värvid.get(tüüp, '')}{tekst}{värvid['lõpp']}"


def kontrolli_url(url):
    if not url.startswith("http"):
        url = "https://" + url
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return värvitud_tulemus(f"✅ {url} töötab", "ok")
        else:
            return värvitud_tulemus(f"⚠️ {url} on tõenäoliselt maas (kood: {response.status_code})", "hoiatus")
    except requests.exceptions.RequestException:
        return värvitud_tulemus(f"❌ {url} ei tööta või on vale", "viga")


print("📡 Veebikontrolli rakendus")
print("============================")
print("Sisesta veebiaadressid komadega eraldatult.")
print("Lõpetamiseks täna mind.")


while True:
    sisend = input("\n🌐 Veebiaadress(id): ").strip().lower()
    if sisend in ["aitäh", "aitah"]:
        print("👋 Aitäh kasutamast!")
        break

    urlid = [u.strip() for u in sisend.split(",") if u.strip()]
    if not urlid:
        print("❗ Palun sisesta vähemalt üks aadress.")
        continue

    for url in urlid:
        tulemus = kontrolli_url(url)
        print(tulemus)
    print()
