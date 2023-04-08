def sieve_of_eratosthenes(n):
    # Tworzymy listę z wartościami True, które oznaczają, że liczby są potencjalnie pierwsze.
    prime_list = [True] * (n+1)
    # 0 i 1 nie są liczbami pierwszymi, więc je pomijamy.
    prime_list[0] = False
    prime_list[1] = False

    # Iterujemy od 2 do pierwiastka z n.
    for i in range(2, int(n**0.5)+1):
        # Jeśli liczba jest potencjalnie pierwsza, to ustawiamy na False wszystkie jej wielokrotności.
        if prime_list[i]:
            for j in range(i**2, n+1, i):
                prime_list[j] = False

    # Zwracamy listę liczb pierwszych.
    prime_numbers = [i for i in range(n+1) if prime_list[i]]
    return prime_numbers


n = 20
prime_numbers = sieve_of_eratosthenes(n)
print(prime_numbers)  # [2, 3, 5, 7, 11, 13, 17, 19]
