def check_palindrome(x):
    given = str(x)
    reversed_string = given[::-1]

    if given == reversed_string:
        return "true"
    else:
        return "false"

print(check_palindrome(-212))