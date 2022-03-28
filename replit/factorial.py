class factorial:
    def __call__(self, num):
        final = 1
        for i in range(1, num + 1):
            final = final * i
        return final


factorial = factorial()
number = input("enter a number to find the factorial of: ")
number = int(number)
print("the factorial of ", number, "is",   factorial(number))
