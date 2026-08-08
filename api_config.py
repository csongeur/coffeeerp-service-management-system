import requests

API_URL = "https://example.com/api"
def szerviz_lekeres():
    valasz = requests.get(
        f"{API_URL}/szerviz_lista.php",
        timeout=20
    )
    valasz.raise_for_status()
    return valasz.json()

def szerviz_uj(adat):
    valasz = requests.post(
        f"{API_URL}/szerviz_uj.php",
        json=adat,
        timeout=20
    )
    valasz.raise_for_status()
    return valasz.json()

def szerviz_modosit(adat):
    valasz = requests.post(
        f"{API_URL}/szerviz_modosit.php",
        json=adat,
        timeout=20
    )
    valasz.raise_for_status()
    return valasz.json()

def szerviz_torol(id):
    valasz = requests.post(
        f"{API_URL}/szerviz_torol.php",
        json={"id": id},
        timeout=20
    )
    valasz.raise_for_status()
    return valasz.json()
