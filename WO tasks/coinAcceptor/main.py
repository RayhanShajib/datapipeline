from coin_acceptor import CoinAcceptor  

def main():
    acceptor = CoinAcceptor()
    print("Program starting.")
    while True:
        print("\n1 - Insert coin")
        print("2 - Show coins")
        print("3 - Return coins")
        print("0 - Exit program")
        choice = input("Your choice: ")
        
        if choice == '1':
            acceptor.insertCoin()
            print("Coin inserted.")
        elif choice == '2':
            amount = acceptor.getAmount()
            print(f"Currently '{amount}' coins in coin acceptor")
        elif choice == '3':
            returned = acceptor.returnCoins()
            print(f"Coin acceptor returned '{returned}' coins.")
        elif choice == '0':
            print("Program ending.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()