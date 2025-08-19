# 1.banka
"""
Nasimulujme si fungování bankovní aplikace, konkrétně žádost o převod peněz z účtu. Na začátku si
vytvoř program balance.txt a do něj vlož nějaké číslo. Toto číslo reprezentuje aktuální zůstatek na účtu.

Přečti hodnotu v souboru, převeď ji na číslo a ulož ji do proměnné account_balance. Čtení souboru i převod
na číslo ošetři pomocí výjimek. Následně se zeptej uživatele (uživatelky), kolik peněz chce převést na jiný účet.
Ošetři pomocí výjimky, že uživatel (uživatelka) zadal(a) číslo. Dále vyvolej ValueError v případě, že zadaná částka
je záporná nebo vyšší než zústatek na účtu. Pokud je vše v pořádku, spočítej nový zůstatek a zapiš ho do souboru balance.txt.
"""

zacatek_na_uctu = 20000
with open("balance.txt", mode="w", encoding="utf-8") as output_file:
    print(zacatek_na_uctu, file=output_file)

with open("balance.txt", mode="r", encoding="utf-8") as input_file:
    try:
        account_balance = int(input_file.read())
    except ValueError:
        print("Soubor neobsahuje číslo")
    except FileNotFoundError:
        print("soubor se zůstatkem nenalezen")

try:
    account_transfer = int(
        input("Zadej číselnou hodnotu kolik penez chceš převést na jiný učet:")
    )
    if account_transfer < 0 or account_balance < account_transfer:
        raise ValueError(
            "částka musí být větší než 0 a menší než aktuální suma na účtě"
        )
    else:
        new_account_balance_num = account_balance - account_transfer
    with open("balance.txt", "w", encoding="utf-8") as soubor:
        print(new_account_balance_num, file=soubor)
    print(f"jako nový zůstatek byla zadána částka {new_account_balance_num} Kč.")
except ValueError:
    print("musíš zadat kladnou číselnou hodnotu menší než tvůj zůstatek")
