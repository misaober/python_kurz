"""# Zadání úkolu 2

Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.

## Část 1

V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO). Toto číslo je jedinečným identifikátorem subjektu,
pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektui. Nejprve se pomocí funkce `input()` zeptej uživatele nebo uživatelky, o kterém subjektu
chce získat informace. S využitím modulu `requests` odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO,
kde `ICO` nahraď číslem, které zadal(ka) uživatel(ka) (např. https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/22834958). S adresou pracuj
jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu `.replace()`, operátor `+` atd. Text, který API vrátí, převeď na JSON a zjisti z něj
obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle `textovaAdresa`). Získané informace vypiš na obrazovku.


## Část 2

Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu. Napiš program, který se zeptá uživatele(ky) na název subjektu,
který chce vyhledat. Následně vypiš všechny nalezené subjekty, které ti API vrátí.

V případě vyhledávání musíme odeslat požadavek typu POST na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat. Request typu POST
pošleme tak, že namísto funkce `requests.get()` použijeme funkci `requests.post()`.

Tentokrát API vrátí počet nalezených subjektů (`pocetCelkem`) a seznam nalezených subjektů `ekonomickeSubjekty`. Tvůj program by měl vypsat obchodní
jména všech nalezených subjektů a jejich identifikační čísla, výstupy odděluj čárkou.
"""

import requests

# část 1
ico = input("Zadej číslené IČO subjektu, který tě zajímá:").strip()
response = requests.get(
    "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/" + ico
)
vystup = response.json()
# print(vystup.keys())
if response.status_code == 200:
    print(vystup["obchodniJmeno"])
    print(vystup["sidlo"]["textovaAdresa"])
else:
    print("Zadané ičo nebylo nalezeno")

# část 2
nazev = input("Zadej název subjektu:").strip()
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = '{"obchodniJmeno": "' + nazev + '"}'
data = data.encode("utf-8")
response_2 = requests.post(
    "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat",
    headers=headers,
    data=data,
)
vystup_2 = response_2.json()
# print(vystup_2.keys())
pocet_subjektu = vystup_2["pocetCelkem"]
print(f"Nalezeno subjektů: {pocet_subjektu}")
for i in range(pocet_subjektu):
    print(
        f"{vystup_2["ekonomickeSubjekty"][i]["obchodniJmeno"]}, {vystup_2["ekonomickeSubjekty"][i]["ico"]}"
    )
