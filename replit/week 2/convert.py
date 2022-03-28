def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')


# Driver Code
if __name__ == '__main__':

    dec_val = int(input("Enter decimal number: "))

    # Calling function
    print("Binary Number:"), DecimalToBinary(dec_val)
