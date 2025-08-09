def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")
if is_palindrome(string):
    print("True")
else:
    print("False")