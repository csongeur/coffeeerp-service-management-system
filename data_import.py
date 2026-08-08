from api_config import szerviz_lekeres

szerviz = []

def adatbazis_frissites():
    adatok = szerviz_lekeres()
    szerviz.clear()
    for sor in adatok:
        szerviz.append([
            str(sor["datum"] or ""),
            str(sor["azonosito"] or ""),
            str(sor["tipus"] or ""),
            str(sor["nev"] or ""),
            str(sor["telefon"] or ""),
            str(sor["ar"] or ""),
            str(sor["polchely"] or ""),
            str(sor["statusz"] or ""),
            str(sor["megjegyzes"] or ""),
            str(sor["megjegyzes2"] or ""),
            str(sor["email"] or ""),
            str(sor["id"])
        ])
adatbazis_frissites()
