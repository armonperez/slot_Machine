import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
#dictionary for the symbols on the slot machine

def check_winnnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # loop through every row 
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

    


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
    #gives key and value 
        for _ in range(symbol_count):
            all_symbols.append(symbol)
#loop through the dictionary


    columns = []
    #Define the columns list
    for _ in range(cols):
    #generate a column for every one that we have 
        column = []
        current_symbols = all_symbols[:]
        #the [:] is used to make a copy of the list not a reference.
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            #removes the first instance of the value in the list.
            column.append(value)
            #add the value to the column.
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            #enumerate gives the index as well as the item.
            if i != len(columns)-1:
                #len(columns)-1  is the maximum index
                print(column[row], end=" | ")
                #The "|" is used if we are not printing the last column
            else:
                print(column[row], end="")
        print()        

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
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
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
    

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

main()