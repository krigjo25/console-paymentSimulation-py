#   Cocaine Machine
import sys
import random as r

def main ():

    """
        Title       :   Cocaine Machine
        author      :   krigjo25
        Description :

    """

    #   Initializing Ammount due
    n = r.randint(5, 1000)

    #   Initializing a list
    coins = (1, 5, 10, 25, 50)

    #   Creating a while loop to iterate the program
    while True:

        #   prompt the user for a coin
        print(f"Amount Due: {n}")
        x = input("Type a coin: ")

        try:
            #   Ensures that user supplied coin is a number
            if x.isalpha() or not x or x.isspace() or int(x) not in coins:
                raise ValueError(f"Error: Please enter a valid number of coins to pay with {coins}")

        except ValueError as e:
            sys.exit(e)

        #   Substract owned coins
        n -= int(x)

        # When x is less than 1, break the loop
        if n < 1:
            break

    print(f"Change Owed: {abs(x)}")



if __name__ == '__main__':
    main()
