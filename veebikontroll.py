import requests

def puhasta_url(url):
    url = url.strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url

def kontrolli(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code < 400:
            print(f"{url} töötab.\n")
        else:
            print(f"{url} on tõenäoliselt maas.\n")
    except:
        print(f"{url} ei tööta või on vale (ära huiia).\n")

print("🌐 Veebilehe kontrollija")
print("Kirjuta 'tsau' või 'aitäh', et lõpetada.\n")

while True:
    sisend = input("Sisesta veebileht (nt delfi.ee): ")
    if sisend.lower() in ["aitäh", "aitah"]:
        print("Aitäh sulle, sa oled kingitus maailmale.")
        break    
    if sisend.lower() in ["tsau"]:
        print("Tsau tsau tsau...")
        break
    if sisend.strip() == "":
        continue

    url = puhasta_url(sisend)
    kontrolli(url)
