#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program asks the user to input two numbers
# The program then tells the user which number is bigger,smaller or equal


def main():
    # this tells the user what number is bigger,smaller or equal

    # input
    number_one = input("Enter the first number: ")
    number_two = input("Enter the second number: ")

    # process & output
    try:
        integer_as_first = int(number_one)
        integer_as_second = int(number_two)

        if integer_as_first == integer_as_second:
            print("The two numbers are equal!")

        if integer_as_first > integer_as_second:
            print("The first number is bigger than the second number!")

        if integer_as_first < integer_as_second:
            print("The second number is bigger than the second number!")

    except Exception:
        print("This is an invaild number!")

    finally:
        print("Done.")


if __name__ == "__main__":
    main()
