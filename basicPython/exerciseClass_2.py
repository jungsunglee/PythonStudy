'''
1. Item common attribute : name : str, price : int, weight : float, isdropable : boolean / method : sale(), discard()
2. WearableItem : effect : str / mothod : wear()
3. UsableItem : effect : str / method : use()
'''

class Item:
    def __init__(self, name: str, price: int, weight: float, isdropable: bool) -> None:
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self) -> None:
        print(f"[{self.name}] is sold with [{self.price}].")

    def discard(self) -> None:
        if self.isdropable == True:
            print(f"[{self.name}] is discarded.")
        else:
            print(f"[{self.name}] colud not be discarded.")

class WearableItem(Item):
    def __init__(self, name: str, price: int, weight: float, isdropable: bool, effect: str) -> None:
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def wear(self):
        print(f"Wear the {self.name} and get the {self.effect}")

class UsableItem(Item):
    def __init__(self, name: str, price: int, weight: float, isdropable: bool, effect: str) -> None:
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"Use the {self.name} and get the {self.effect}")

newAmor = WearableItem("NEWAMOR", 1000, 22.5, False, "Defance ability +50")
oldAmor = WearableItem("OLDAMOR", 500, 45.5, True, "Defance ability +25")

newAmor.wear()
oldAmor.wear()
oldAmor.discard()
newAmor.discard()

newAmor.sale()

newSword = UsableItem("HEROSWARD", 10000, 5.5, False, "Attack ability +300")
newSword.use()
newSword.sale()
        