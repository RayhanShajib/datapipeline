class SodaBottle:
    brand: str
    cap_open: bool
    def __init__(self, brand) -> None:
        self.brand = brand
        self.cap_open = False
        return None
    def openBottle(self) -> None:
        if self.cap_open != True:
            print("sihhh...")
            self.cap_open = True
            return None
    def drink(self) -> None:
        if self.cap_open == False:
            print("Can't drink from a closed bottle...")
        else:
            print(f"Glunk, Glunk! mm.. Tastes like {self.brand}!")
        return None
    def __str__(self) -> str:
        return self.brand