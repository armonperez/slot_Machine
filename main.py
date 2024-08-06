MAX_LINES = 3
#global variable can be set like this 
MAX_BET = 100
MIN_BET = 5
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
        # isdigit() is used to tell us if this is a valid whole number
            amount = int(amount)
            #done after isdigit() because we need to frst check its a valid number
            if amount > 0:
                break
            #break ends the while loop 
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines 

def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
        # isdigit() is used to tell us if this is a valid whole number
            amount = int(amount)
            #done after isdigit() because we need to frst check its a valid number
            if MIN_BET <= amount <= MAX_BET:
                break
            #break ends the while loop 
            else:
                print(f"Amount must be between {MIN_BET - MAX_BET}.")
                #add values into a string, converts variables into str if possible
        else:
            print("Please enter a number.")
    return amount
    




def main():
    balance = deposit()

    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance :
            print(
                f" You do not have enough to bet that amount, your current balance is ${balance}")
        else:
            break 
# above checks to make sure we cannot bet more than our current balance.
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    



main()