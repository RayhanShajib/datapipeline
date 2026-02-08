from file_handler import FileHandler

filename = "inventory.csv"
inventory_file = FileHandler(filename)
rows = inventory_file.read() # use read method for the previously crated object
print(f"####{filename}####")

for row in rows:
    print(row)

print(f"####{filename}####")