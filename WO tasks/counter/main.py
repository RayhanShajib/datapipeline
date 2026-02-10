from counter import Counter

def Main():
    counter = Counter()
    while True:
        print("\nChoose an action:")
        print("1. Add count")
        print("2. Get count")
        print("3. Zero count")
        print("4. Exit program")
        choice = input("choice: ")

        if choice == "1":
            counter.addCount()
            print("Count incremented.")
        elif choice == "2":
            print(f"Current count: {counter.getCount()}")
        elif choice == "3":
            counter.zeroCount()
            print("Count reset to zero.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Main()

