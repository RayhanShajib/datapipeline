class CoinAcceptor:
    def __init__(self):
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self) -> None:
        self.__amount += 1
        self.__value += 0.25

    def getAmount(self) -> int:
        return self.__amount
    
    def returnCoins(self) -> int:
        coins_returned = self.__amount
        self.__amount = 0
        self.__value = 0.0
        return coins_returned

    def getValue(self) -> float:
        return self.__value
