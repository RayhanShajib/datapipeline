class User:
    def __init__(self, fName: str, lName: str) -> None:
        self.fName = fName
        self.lName = lName
        return None

    def fullName(self) -> None:
        print(self.fName+ " " + self.lName)
        return None