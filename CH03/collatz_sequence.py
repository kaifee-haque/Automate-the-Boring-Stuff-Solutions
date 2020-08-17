#! python3
"""Takes a number from the user and prints its collatz sequence."""

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    userNumber = int(input("Enter a positive integer: "))
    while userNumber != 1:
        userNumber = collatz(userNumber)
        print(userNumber)
except ValueError:
    print("Input must be a positive integer.")
