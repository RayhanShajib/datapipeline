class Entity:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def interact(self):
        return f"{self.name} at {self.position}"


class Player(Entity):
    def __init__(self, name, position, health=100):
        super().__init__(name, position)
        self.health = health

    def interact(self):
        return f"Player {self.name} - Health: {self.health}"


class NPC(Entity):
    def __init__(self, name, position, dialogue):
        super().__init__(name, position)
        self.dialogue = dialogue

    def interact(self):
        return f"NPC {self.name}: '{self.dialogue}'"


class Object(Entity):
    def __init__(self, name, position, obj_type):
        super().__init__(name, position)
        self.obj_type = obj_type

    def interact(self):
        return f"Object {self.name} - Type: {self.obj_type}"


def interact_with_all(entities):
    print("\n=== Polymorphism Demo ===")
    for i, entity in enumerate(entities, 1):
        print(f"{i}. {entity.interact()}")


def add_entity(entities):
    print("\n1. Player  2. NPC  3. Object")
    choice = input("Choose (1-3): ")
    name = input("Name: ")
    pos = input("Position (x,y,z): ").split(',')
    position = tuple(map(int, pos)) if len(pos) == 3 else (0, 0, 0)

    if choice == '1':
        health = int(input("Health: ") or 100)
        entities.append(Player(name, position, health))
    elif choice == '2':
        dialogue = input("Dialogue: ")
        entities.append(NPC(name, position, dialogue))
    elif choice == '3':
        obj_type = input("Type: ")
        entities.append(Object(name, position, obj_type))

    print(f"Added {name}!")


def main():
    entities = [
        Player("Hero", (0, 0, 0), 100),
        NPC("Guard", (1, 1, 0), "Stop right there!"),
        Object("Sword", (2, 2, 0), "weapon")
    ]

    while True:
        print("\n1 - Add Entity")
        print("2 - Interact with Entities")
        print("3 - Exit")

        choice = input("Choice: ")

        if choice == '1':
            add_entity(entities)
        elif choice == '2':
            interact_with_all(entities)
        elif choice == '3':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
