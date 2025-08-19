# 2. transformace # moje reseni inspirovane AI
"""Stáhněte si soubor words.txt a zpracujte z něj výstupní soubor ve formátu JSON obsahující slovník. Klíče budou písmena a
hodnoty seznamy slov, které začínají písmenem v klíči. Pokud na nějaké písmeno žádná slova nezačínají, tak ve výstupu toto písmeno nebude.
Seřaďte tyto seznamy podle abecedy. Zajistěte, aby i klíče ve výstupním JSON souboru byly seřazeny a data byla odsazena
 čtyřmi mezerami pro lepší čitelnost člověkem."""

import json

with open("words.txt", encoding="utf-8") as file:
    slova = file.read().split()

slova = sorted(slova)
print(slova)

seznam_pismen = []
slovnik = {}
for line in slova:
    pismeno = line[0]
    if pismeno not in seznam_pismen:
        seznam_pismen.append(pismeno)
        slovnik[pismeno] = []
        slovnik[pismeno].append(line)
    else:
        slovnik[pismeno].append(line)
print(seznam_pismen)
print(slovnik)

with open("output.json", mode="w", encoding="utf-8") as file:
    json.dump(slovnik, file, indent=4)
