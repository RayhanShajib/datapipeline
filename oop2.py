from sodaBottle import SodaBottle


class Main:
    def __init__(self) -> None:
        print("Program starting")
        bottle_cola = SodaBottle("coca cola")
        print("Bottle brand is:", bottle_cola.brand)
        print(bottle_cola)
        print(bottle_cola.brand)
        bottle_cola.drink()
        bottle_cola.openBottle()
        bottle_cola.drink()
        print("close the program")
        return None

if __name__ == "__main__":
    app = Main()
