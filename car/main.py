from car import Car

class Main:
    def __init__(self) -> None:
        car1 = Car("red", 200.0)
        car2 = Car("blue", 300)

        car1.start()
        car2.start()
        print(car1.max_speed)

        return None

if __name__ == "__main__":
    app = Main()