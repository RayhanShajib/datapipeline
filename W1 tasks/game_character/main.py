from abc import ABC, abstractmethod


class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass


class Warrior(GameCharacter):
    def attack(self):
        return f"{self.name} swings a mighty sword!"

    def defend(self):
        return f"{self.name} raises a heavy shield!"


class Mage(GameCharacter):
    def attack(self):
        return f"{self.name} casts a fireball spell!"

    def defend(self):
        return f"{self.name} creates a magical barrier!"


class Archer(GameCharacter):
    def attack(self):
        return f"{self.name} shoots a precise arrow!"

    def defend(self):
        return f"{self.name} dodges with quick reflexes!"


def simulate_battle(characters):
    print("\n--- Battle Simulation ---")
    for character in characters:
        print(character.attack())
        print(character.defend())
        print()


def create_character():
    try:
        name = input("Enter character name: ")
        print("Select character type:")
        print("1 - Warrior")
        print("2 - Mage")
        print("3 - Archer")
        choice = int(input("Enter choice: "))

        if choice == 1:
            return Warrior(name)
        elif choice == 2:
            return Mage(name)
        elif choice == 3:
            return Archer(name)
        else:
            print("Invalid choice!")
            return None
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None


def main():
    characters = []

    while True:
        try:
            print("\nMenu:")
            print("1 - Create Character")
            print("2 - Simulate Battle")
            print("0 - Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                character = create_character()
                if character:
                    characters.append(character)
                    print(f"{character.name} created successfully!")

            elif choice == 2:
                if characters:
                    simulate_battle(characters)
                else:
                    print("No characters available for battle!")

            elif choice == 0:
                print("Goodbye!")
                break

            else:
                print("Invalid menu choice!")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()
