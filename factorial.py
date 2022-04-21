#!/usr/bin/env python3
# Created by Marc Coffi
# Created in April 2022
# Factorial


def main():
    # Defining variables
    counter = 0
    factorial = 1
    user_input = input("Enter a whole number: ")
    print("")
    try:
        # Casting user input
        user_num = int(user_input)
        if user_num >= 0:
            while True:
                counter += 1
                print("Tracking {} times through loop.".format(counter))
                # Do the factorial calculation
                factorial = factorial * counter
                if counter >= user_num:
                    break

        else:
            exit()
    except:
        print("Invalid input.\nNot a proper number")
        exit()
    # Display the
    print("{}!= {}".format(user_num, factorial))
    print("")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
