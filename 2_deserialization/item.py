from dataclasses import dataclass

@dataclass
class Item:
    SEPARATOR = ","
# The @dataclass decorator will automatically create an __init__
# method that initializes the following attributes.
    name: str
    value: float
    category: str
    weight: float
    @staticmethod
# The @staticmethod decorator is used to define a method that
# belongs to the class rather than an instance of the class. This
# means you can call the method on the class itself, without
# needing to create an instance.
    def deserialize(row: str) -> 'Item':

# Expecting row that contains => "name",value,"category",weight
# The deserialize method is a static method that takes a string row as
# input and returns an Item object.
# It splits the input string row using the SEPARATOR (a comma in this
# case) and assigns the resulting values to the corresponding
# attributes of the Item class.
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
