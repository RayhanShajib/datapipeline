class TemperatureConverter:
    def __init__(self) -> None:
        self.__temperature = 0
    
    def setTemperature(self, temperature: float) -> None:
        self.__temperature = temperature

    def toCelsius(self) -> float:
        return self.__temperature
    
    def toFahrenheit(self) -> float:
        return (self.__temperature * 9/5) + 32
    
    def toKelvin(self) -> float:
        return self.__temperature + 273