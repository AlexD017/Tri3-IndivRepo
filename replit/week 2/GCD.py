class GCD:
    def __init__(self):
        self.factor = [0, 1]

    def __call__(self, num1, num2):
        if num1 == 0:
            return num1
        while num2 != 0:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1


def main():
    findgcd = GCD()
    a = int(input(" Enter the First Value: "))
    b = int(input(" Enter the Second Value: "))
    gcd = findgcd(a, b)
    print("\n GCD of {0} and {1} is: {2}".format(a, b, gcd))


if __name__ == "__main__":
    main()
