# vyplata znovu
"""Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

Nejprve tyto informace vypište na terminál
Poté program upravte tak, aby vypsal tyto výsledky do souboru"""

vykaz = []
with open("vykaz.txt", encoding="utf-8") as file:
    for line in file:
        hodiny = int(line.strip())
        vykaz.append(hodiny)
print(f"seznam odpracovaných hodin za každý měsíc: {vykaz}")

sazba = float(input("zadej hodinovou sazbu:"))

seznam_mesicni_vyplata = []
# výpočet průměrné výplaty na jeden měsíc
for zaznam in vykaz:
    mesicni_vyplata = zaznam * sazba
    seznam_mesicni_vyplata.append(mesicni_vyplata)

# napíše to všechno vedle sebe
with open("mesicni_vyplata.txt", "w", encoding="utf-8") as output_file:
    print(seznam_mesicni_vyplata, file=output_file)

# napise to zaznamy pod sebe
with open("mesicni_vyplata.txt", "w", encoding="utf-8") as output_file:
    for line in seznam_mesicni_vyplata:
        print(line, file=output_file)


# lektorka to má jednodušeji, napsala ten výpočet rovnou do té fce toho zápisu:
with open("vyplata.txt", mode="w", encoding="utf-8") as output_file:
    for number in lines:
        wage = number * hourly_wage
        print(wage, file=output_file)
