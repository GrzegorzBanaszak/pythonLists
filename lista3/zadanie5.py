
# W zadanu korzystam z recursion
def factorial_number(number):
    if number == 1:
        return 1
    return number * factorial_number(number - 1)


print(factorial_number(4))
print(factorial_number(6))
