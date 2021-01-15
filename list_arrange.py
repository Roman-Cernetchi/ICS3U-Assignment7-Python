#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program returns the odd numbers in a list


def odd_indices(list_U):

    count = 0

    for i in list_U:
        if count % 2 == 1:
            list_U.append(i)
        count += 1

    return count


def main():
    # This function handles input and prints a 2D array

    list_U = []

    # input
    while True:
        # Input
        amount_input = input("Enter how many numbers you will use: ")
        print("")
        try:
            amount = int(amount_input)
            break
        except Exception:
            print("This was not an integer")

    loop_counter = 0

    while loop_counter < amount:
        loop_counter = loop_counter + 1

        while True:
            try:
                number_input = input("Enter a chosen number: ")
                number = int(number_input)
                list_U.append(number)

                if loop_counter < amount:
                    break

                odd_element = odd_indices(list_U)

                print("")
                print("The odd elements in the list are: {0}"
                      .format(odd_element))
                break

            except Exception:
                # output
                print("Invalid input, try again.")


if __name__ == "__main__":
    main()
