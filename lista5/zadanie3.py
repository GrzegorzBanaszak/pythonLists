def revers_number(num):
    revers = list(map(str, str(num)))
    revers.reverse()
    palindrome = is_palindrome(revers)
    return int("".join(revers)), palindrome


def is_palindrome(arr):
    palindrome = True
    first_pointer = 0
    second_pointer = len(arr) - 1
    while first_pointer < second_pointer:
        if arr[first_pointer] == arr[second_pointer]:
            first_pointer += 1
            second_pointer -= 1
            continue
        else:
            palindrome = False
            break

    return palindrome


reversed, poli = revers_number(12321)

print(reversed, poli)
