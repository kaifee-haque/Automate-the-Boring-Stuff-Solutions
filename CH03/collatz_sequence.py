def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

userNumber = int(input("Enter a number: "))
while(userNumber != 1):
    userNumber = collatz(userNumber)
    print(userNumber)
