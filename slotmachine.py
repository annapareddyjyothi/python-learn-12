import random

def spin_reels():
    """Simulate spinning the slot machine reels."""
    symbols = ["🍒", "🍋", "🍉", "⭐", "🔔"]  # Symbols for the reels
    return [random.choice(symbols) for _ in range(3)]  # Spin 3 reels

def calculate_payout(reels, bet):
    """Calculate the payout based on the reels and bet."""
    if reels[0] == reels[1] == reels[2]:  # All three symbols match
        payout_multiplier = 5
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:  # Two symbols match
        payout_multiplier = 2
    else:  # No matches
        payout_multiplier = 0
    
    return bet * payout_multiplier

def display_reels(reels):
    """Display the slot machine reels."""
    print(f" | {reels[0]} | {reels[1]} | {reels[2]} | ")

def slot_machine():
    """Main function to play the slot machine."""
    print("Welcome to the Slot Machine!")
    balance = 100  # Starting balance for the player

    while balance > 0:
        print(f"\nYour current balance is: ${balance}")
        try:
            bet = int(input("Enter your bet (or 0 to quit): "))
            if bet == 0:
                print("Thanks for playing! Goodbye!")
                break
            if bet > balance:
                print("You don't have enough balance for that bet!")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid bet.")
            continue

        # Spin the reels and display the result
        reels = spin_reels()
        print("\nSpinning...")
        display_reels(reels)

        # Calculate payout
        payout = calculate_payout(reels, bet)
        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
            balance += payout
        else:
            print("No matches! You lost your bet.")
            balance -= bet

    if balance <= 0:
        print("\nYou're out of money! Better luck next time!")

if __name__ == "__main__":
    slot_machine()
