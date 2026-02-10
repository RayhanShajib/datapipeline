from coin_acceptor import CoinAcceptor  

def main():
    acceptor = CoinAcceptor()
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    
    while True:
        try:
            coin_value = float(input("Insert coin(0 return, -1 exit): "))
            if coin_value == -1:
                print("Exiting program.")
                print("Thank you for using the program.")
                print("Program ending.")
                break
            elif coin_value == 0:
                returned_amount, returned_value = acceptor.returnCoins()
                print("Returning coins...")
                print(f"{returned_amount} coins with {returned_value}€ value returned.")
                print("Inserted coins = 0, value = 0€")
            elif coin_value > 0:
                acceptor.insertCoin(coin_value)
                print("Inserting...")
                print(f"Inserted coins = {acceptor.getAmount()}, value = {acceptor.getValue()}€")
            else:
                print("Invalid coin value. Please enter a positive value, 0 to return, or -1 to exit.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()