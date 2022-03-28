def factors():
    num = int(input("Enter any number: "))
    findfactors(num)


def findfactors(number):
    print("Factors of the given number {0} is:".format(number))

    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()


factors()
