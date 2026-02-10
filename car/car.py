class Car:
    def __init__(self, color: str, max_speed: float) -> None:
        self.color = color
        self.max_speed = max_speed

    def start(self) -> None:
        print(self.color, "car is started")
    
    def getSpeed(self) -> float:
        return self.max_speed