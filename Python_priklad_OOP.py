# celková hodnota balíků podruhé - FUNGUJE
"""
Vedení společnosti si uvědomilo, že do hodnoty cenných balíků v autě by se neměly započítávat balíky, které už byly doručeny, 
protože již byly předány příjemci a nebudou tedy ukradeny nebo zničeny.

Uprav kód, který vytváří balíky, aby byl jeden balík vytvořený ve stavu doručen.
Uprav cyklus, aby započítal hodnotu pouze těch cenných balíků, které jsou ve stavu nedoručen. """
class Package:
    def __init__(self, address, weight, state ="nedoručen"):
        self.address = address
        self.weight = weight
        self.state = state
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} a je ve stavu {self.state}."
    def delivery_price(self):
        if self.weight <= 10:
            return 129
        elif self.weight <=20:
            return 159
        else:
            return 359
    def deliver(self):
        if self.state == "doručen":
            return f"Balík již byl doručen."
        else:
            self.state = "doručen"
            return f"doručení uloženo."
class ValuablePackage (Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value
    def __str__(self):
        return super().__str__() + f" Cena baliku je {self.value} Kč."
    def delivery_price(self):
        return super().delivery_price() + self.value*0.05
    
balik= Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
balicek = Package("Doubraviska, Praha", 22 , "doručen")
drahy_balik = ValuablePackage("harrachov 33", 7, "nedoručen", 3000)
drahy_balik_2 = ValuablePackage("harrachov 33", 9, "nedoručen", 5000)
drahy_balik_3 = ValuablePackage("harrachov 33", 11, "doručen", 7000)
package_list = [balik, balicek, drahy_balik, drahy_balik_2, drahy_balik_3]

total_value = 0
for item in package_list:
    #zkontroluju, zda jde o valuable package
    if isinstance(item, ValuablePackage):
        if getattr(item, "state") == "nedoručen":
            total_value = total_value + item.value
print(total_value)

total_value_1 = 0
for item in package_list:
    if hasattr(item, "value"):
        if getattr(item, "state") == "nedoručen":
            total_value_1 += item.value
print(total_value_1)