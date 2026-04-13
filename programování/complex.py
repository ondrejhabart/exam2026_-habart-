objednavky = [
    {"cislo": 2001, "zakaznik": "Jan Novák", "zaplaceno": True, "polozka": "Myš", "mnozstvi": 2, "cena_kus": 350},
    {"cislo": 2002, "zakaznik": "Petra Svobodová", "zaplaceno": True, "polozka": "Monitor", "mnozstvi": 1, "cena_kus": 4200},
    {"cislo": 2001, "zakaznik": "Jan Novák", "zaplaceno": True, "polozka": "Klávesnice", "mnozstvi": 1, "cena_kus": 1200},
    {"cislo": 2003, "zakaznik": "Karel Dvořák", "zaplaceno": False, "polozka": "USB disk", "mnozstvi": 3, "cena_kus": 250},
    {"cislo": 2004, "zakaznik": "Anna Malá", "zaplaceno": True, "polozka": "Notebook", "mnozstvi": 1, "cena_kus": 15000},
    {"cislo": 2005, "zakaznik": "Lukáš Černý", "zaplaceno": True, "polozka": "", "mnozstvi": 2, "cena_kus": 500},
    {"cislo": 2002, "zakaznik": "Petra Svobodová", "zaplaceno": True, "polozka": "Kabel", "mnozstvi": 0, "cena_kus": 150},
    {"cislo": 2006, "zakaznik": "Eva Veselá", "zaplaceno": True, "polozka": "Sluchátka", "mnozstvi": 1, "cena_kus": -300},
    {"cislo": 2004, "zakaznik": "Anna Malá", "zaplaceno": True, "polozka": "Myš", "mnozstvi": 1, "cena_kus": 300},
    {"cislo": 2007, "zakaznik": "Tomáš Bílý", "zaplaceno": True, "polozka": "Tablet", "mnozstvi": 1, "cena_kus": 8000},
    {"cislo": 2005, "zakaznik": "Lukáš Černý", "zaplaceno": True, "polozka": "Klávesnice", "mnozstvi": 1, "cena_kus": 1200},
    {"cislo": 2008, "zakaznik": "Marek Novotný", "zaplaceno": False, "polozka": "Monitor", "mnozstvi": 1, "cena_kus": 4000},
    {"cislo": 2007, "zakaznik": "Tomáš Bílý", "zaplaceno": True, "polozka": "Obal", "mnozstvi": 2, "cena_kus": 200},
    {"cislo": 2009, "zakaznik": "Jana Králová", "zaplaceno": True, "polozka": "Telefon", "mnozstvi": 1, "cena_kus": 10000},
    {"cislo": 2009, "zakaznik": "Jana Králová", "zaplaceno": True, "polozka": "Nabíječka", "mnozstvi": 1, "cena_kus": 0},
    {"cislo": 2010, "zakaznik": "Petr Horák", "zaplaceno": True, "polozka": "Myš", "mnozstvi": 1, "cena_kus": 350},
    {"cislo": 2010, "zakaznik": "Petr Horák", "zaplaceno": True, "polozka": "Klávesnice", "mnozstvi": 1, "cena_kus": "abc"},
    {"cislo": 2011, "zakaznik": "Lucie Malá", "zaplaceno": True, "polozka": "Notebook", "mnozstvi": 1, "cena_kus": 20000},
    {"cislo": 2011, "zakaznik": "Lucie Malá", "zaplaceno": True, "polozka": "Taška", "mnozstvi": 1, "cena_kus": 800},
    {"cislo": 2012, "zakaznik": "David Svoboda", "zaplaceno": True, "polozka": "Monitor", "mnozstvi": 1, "cena_kus": 5000},
    {"cislo": 2012, "zakaznik": "David Svoboda", "zaplaceno": True, "polozka": "Kabel", "mnozstvi": 1, "cena_kus": 200},
    {"cislo": 2006, "zakaznik": "Eva Veselá", "zaplaceno": True, "polozka": "Myš", "mnozstvi": 1, "cena_kus": 300},
    {"cislo": 2003, "zakaznik": "Karel Dvořák", "zaplaceno": False, "polozka": "Myš", "mnozstvi": 1, "cena_kus": 300}
]

vybrani = []

for o in objednavky:
    if o["zaplaceno"] == True and o["mnozstvi"] > 0 and type(o["cena_kus"]) == int:
        if o["cena_kus"] > 0:
            
            o["celkem"] = o["mnozstvi"] * o["cena_kus"]
            
            uz_tam_je = False
            for e in vybrani:
                if e["cislo"] == o["cislo"]:
                    e["celkem"] = e["celkem"] + o["celkem"]
                    uz_tam_je = True
            
            if uz_tam_je == False:
                vybrani.append(o)

vybrani.sort(key=lambda x: x["celkem"], reverse=True)

print("Zpracované objednávky:")
print("________________________________________________")

for o in vybrani:
    print(f"Objednávka: {o['cislo']} Zákazník: {o['zakaznik']} Celkem: {o['celkem']} Kč")