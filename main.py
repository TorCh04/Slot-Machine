# Python Slot Machine
import random

def spinRow():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    # For every iteration in range 3 return a random symbol
    return [random.choice(symbols) for _ in range(3)]

def printRow(row):
    print("*************")
    # Joins each row by a space
    print(" | ".join(row))
    print("*************\n")

def getPayout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 100
    print("**************************")
    print("Welcome to the Casino")
    print("Symobls: 🍒 🍉 🍋 🔔 ⭐")
    print("*************************")

    # Game continues as you have money
    while balance > 0:
        print(f"Current balance: £{balance}")
        
        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid bet!")
            continue
        
        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spinRow()
        print("Spinning...\n")
        printRow(row) 

        payout = getPayout(row, bet)

        if payout > 0:
            print(f"You won £{payout}")
        else:
            print("L bozo you lost")

        balance += payout   

        playAgain = input("More spins? (y/n): ").lower()

        if playAgain != "y":
            break
        
        if balance == 0:
            print("\nYou are out of money")
            retry = input("Sell your soul for more spins? (y/n): ").lower()
            if retry == "y":
                balance += 100

    print("*********************************************")
    print(f"Game Over! Your final balance is £{balance}")
    print("*********************************************")


if __name__ == "__main__":
    main()