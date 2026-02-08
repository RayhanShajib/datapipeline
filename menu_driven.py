class Menu:
    def greeting(self) -> None:
        print("Welcome to the menu!")

    def hello_world(self) -> None:
        print("Hello, World!")

    def askChoice(self) -> int:
        choice = input("Enter your choice: ")
        return int(choice)

    def run(self) -> None:
        self.greeting()
        while True:
            print("1. Hello World")
            print("2. Exit")
            choice = self.askChoice()
            if choice == 1:
                self.hello_world()
            elif choice == 2:
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu = Menu()
    menu.run()
