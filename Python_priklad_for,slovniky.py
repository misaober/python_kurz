"""
Pohlédněte na následující reprezentaci receptu:
Uložte si tuto strukturu do proměnné recept na začátek nového programu. Vypište pomocí funkce print
kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
"""

recept = {
    "nazev": "Batáty se šalvějí a pancettou",
    "narocnost": "stredni",
    "doba": 30,
    "ingredience": [
        ["batát", "1", "15 kč"],
        ["olivový olej", "2 lžíce", "2 kč"],
        ["pancetta", "4-6 plátků", "21 kč"],
        ["přepuštěné máslo", "2 lžíce", "5 kč"],
        ["mletý černý pepř", "1/2 lžičky", "0.5 kč"],
        ["sůl", "1/2 lžičky", "0.1 kč"],
        ["muškátový oříšek", "špetka", "1 kč"],
        ["česnek", "2 stroužky", "1 kč"],
        ["šalvějové lístky", "20-25", "12 kč"],
    ],
}
cena_jidla = 0
for ingredience in recept["ingredience"]:
    cena_s_kc = ingredience[2]
    cena_bez_kc = cena_s_kc.strip(" kč")
    cena_jidla += float(cena_bez_kc)
cena_jidla = math.ceil(cena_jidla)
print(f"cena jidla je {cena_jidla}.")

for ingredience in recept["ingredience"]:
    cena_jidla + -float((ingredience[2]).strip(" kč"))
print(f"cena jidla je {cena_jidla}.")
