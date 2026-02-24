from file_handler import FileHandler
from Item import Item

class Main:
    filename = "3_serialization/inventory.csv"
    inventory_file = FileHandler(filename)
    rows = inventory_file.read()  # use read method for the previously crated object
    print(f"#### inventory ####")
    inventory: list[Item] = []

    for row in rows:
        item = Item.deserialize(row)
        inventory.append(item)
        item.display_price()
        print(item)

    print(f"#### inventory ####")
    feed = input(f"Change item value (enter 1 - {len(inventory)}): ")
    print(feed)

    try:
        index = int(feed) -1 
        feed = input(f"Set new value for{inventory[index].name}: ")
        inventory[index].set_value(float(feed)) 
    except Exception:
        print("Oops, something went wrong.")

    print("serializing item into rows.")
    print("## ")


if __name__ == "__main__":
    app = Main()
