#!/usr/bin/env python3


# Created By: Julien Lamoureux
# Date: November 8, 2023
# This program displays the factorial of all the numbers from 0 to the user's number


def main():
    # get the user number as a string
    print(
        "This program displays the factorial of all the numbers from 0 to the user's number."
    )
    user_num_string = input("Enter your integer: ")

    # initialize the counter and factorial to 1
    counter = 1
    factorial = 1

    try:
        # convert user number to an integer
        user_num_int = int(user_num_string)

        # if the user number is less than 0, tell the user to enter a positive integer
        if user_num_int < 0:
            print("{} is not a positive integer".format(user_num_string))
        else:
            # otherwise while the counter is less than or equal to the user number
            while True:
                # display the tracking of the loop
                print("Tracking {} times through loop".format(counter))

                # multiply the counter to the factorial
                factorial = factorial * counter

                # increment the counter
                counter = counter + 1
                if counter > user_num_int:
                    # if the counter is greater than the user num, stop the loop
                    break

            # display the factorial of all the numbers from 0 to the user's number
            print("{0}! = {1}".format(user_num_string, factorial))
    except:
        # if the number is not an integer, then tell them their input is invalid
        print(
            "\n{} is not a valid integer. Please enter a positive integer.".format(
                user_num_string
            )
        )


if __name__ == "__main__":
    main()
