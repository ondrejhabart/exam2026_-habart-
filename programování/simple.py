objednavky = [
    {"cislo": 1001, "zakaznik": "Jan Novák", "zaplaceno": True, "polozka": "Myš", "mnozstvi": 2, "cena_kus": 350},
    {"cislo": 1001, "zakaznik": "Jan Novák", "zaplaceno": True, "polozka": "Klávesnice", "mnozstvi": 1, "cena_kus": 1200},
    {"cislo": 1002, "zakaznik": "Petra Svobodová", "zaplaceno": False, "polozka": "Monitor", "mnozstvi": 1, "cena_kus": 4200},
    {"cislo": 1003, "zakaznik": "Karel Dvořák", "zaplaceno": True, "polozka": "USB disk", "mnozstvi": 3, "cena_kus": 250},
    {"cislo": 1004, "zakaznik": "Anna Malá", "zaplaceno": True, "polozka": "Notebook", "mnozstvi": 1, "cena_kus": 15000},
    {"cislo": 1004, "zakaznik": "Anna Malá", "zaplaceno": True, "polozka": "Myš", "mnozstvi": 1, "cena_kus": 300},
]

vybrani = []

for o in objednavky:
    if o["zaplaceno"] == True and o["mnozstvi"] > 0 and type(o["cena_kus"]) == int:
        
        aktualni_radek_celkem = o["mnozstvi"] * o["cena_kus"]
        
        uz_tam_je = False
        for e in vybrani:
            if e["cislo"] == o["cislo"]:
                e["celkem"] = e["celkem"] + aktualni_radek_celkem
                uz_tam_je = True
        
        if uz_tam_je == False:
            o["celkem"] = aktualni_radek_celkem
            vybrani.append(o)

vybrani.sort(key=lambda x: x["celkem"], reverse=True)

print("Zpracované objednávky:")
print("________________________________________________")

for o in vybrani:
    print(f"Objednávka: {o['cislo']} Zákazník: {o['zakaznik']} Celkem: {o['celkem']} Kč")