#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program returns the odd numbers in a list


def odd_indices(list_U):

    list2 = []
    count = 0
    loop_counter = 0

    for single_element in list_U:
        if loop_counter % 2 == 1:
            list2.append(single_element)
        loop_counter += 1

    return list2


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
        loop_counter += 1
        while True:
            try:
                number_input = input("Enter a chosen number: ")
                number = int(number_input)
                list_U.append(number)
                break
            except Exception:
                # output
                print("Invalid input, try again.")

    list2 = odd_indices(list_U)

    print("")
    print(list_U)
    print("The odd elements in the list are: {0}".format(list2))


if __name__ == "__main__":
    main()
