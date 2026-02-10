from temperature_converter import TemperatureConverter

def Main():
    converter = TemperatureConverter()
    print("\nProgram starting...")
    print("\nInitializing Temperature Converter...")
    print("\nTemperature Converter initialized.")
    while True:
        print("\noptions: ")
        print("1. Set temperature")
        print("2. Convert to Celsius")
        print("3. Convert to Fahrenheit")
        print("4. Convert to Kelvin")
        print("5. Exit program")
        choice = input("choice: ").strip()
        
        if choice == '1':
            try:
                temp = float(input("Enter temperature: "))
                converter.setTemperature(temp)
                print(f"Temperature set to {temp}°C.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '2':
            print(f"Temperature in Celsius: {converter.toCelsius()}°C")
        elif choice == '3':
            print(f"Temperature in Fahrenheit: {converter.toFahrenheit()}°F")
        elif choice == '4':
            print(f"Temperature in Kelvin: {converter.toKelvin()}K")
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Main()