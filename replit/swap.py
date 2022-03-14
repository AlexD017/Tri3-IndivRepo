def numbswap(a, b):
    var = a
    a = b
    b = var
    print("After Swapping two Numbers", (a, b))


Number1 = int(input("Enter first number: "))
Number2 = int(input("Enter second number: "))
print("Before Swapping two Numbers", (Number1, Number2))
numbswap(Number1, Number2)