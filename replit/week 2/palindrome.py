import re


class Palindrome:
    # function to check string is
    # palindrome or not
    def isPalindrome(s):
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # Using predefined function to
        # reverse to string print(s)
        rev = ''.join(reversed(s))

        # Checking if both string are
        # equal or not
        if (s == rev):
            return True
        return False

    # main function
    s = input(str("Enter a statement/word: "))
    ans = isPalindrome(s)

    if (ans):
        print(f"{s} is a Palindrome")
    else:
        print(f"{s} is not a Palindrome")