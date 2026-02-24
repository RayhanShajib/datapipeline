from dataclasses import dataclass

@dataclass
class Item:
    SEPARATOR = ","
    name: str
    value: float
    category: str
    weight: float
    @staticmethod
    def deserialize(row: str) -> 'Item':
        columns = row.split(Item.SEPARATOR)  # Comma Separated Values
        item = Item(
        columns[0],  # name
        float(columns[1]),  # value
        columns[2],  # category
        float(columns[3]),  # weight
    )
        return item
    def display_price(self) -> None:
        print(f"{self.name} costs {self.value} €.")
        return None
    
    def set_value(self, new_value: float) -> None:
        if new_value < 0:
            print("Value can't be negative.")
        else:
            self.value = new_value
    
