def reverse_integer(x):
    negative = False
    if x<0:
        x *= -1
        negative = True

    given = str(x)
    reversed_string = given[::-1]
    reversed_int = int(reversed_string)

    if reversed_int > 2147483647:
        return 0

    if negative:
        reversed_int *= -1

    return reversed_int

print(reverse_integer(1534236469))