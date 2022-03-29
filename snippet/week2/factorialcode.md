### <a href="https://alexd017.github.io/Tri3-IndivRepo/">Back</a>

### Code Snippet for factorial.py

    class factorial:
        def __call__(self, num):
            final = 1
            for i in range(1, num + 1):
                final = final * i
            return final
    factorial = factorial()
    number = input("Enter a number to find the factorial of: ")
    number = int(number)
    print("The factorial of ", number, "is",   factorial(number))
