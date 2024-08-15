"""Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
Napište program, který vygeneruje všechna prvočísla menší než N
pomocí algoritmu Eratosthenovo síto.

Eratosthenovo síto funguje tak, že postupně "odškrtáváte" násobky každého čísla počínaje 2,
které jsou tím pádem složená čísla. Čísla, která zůstanou neodškrtnutá, jsou prvočísla.
"""

""" prvočísla do hodnoty n """
# def is_prime(n: int):
#     if n <2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# primes = []
# for n in range(2, 1000):
#     if is_prime(n):
#         primes.append(n)
#
# # print(primes)
#
# if __name__ == "__main__":
#     n = 100
#     for i in range(2, n+1):
#         print(f'{i} = {is_prime(i)}',end=", ")

"""Sive of Erathothenes"""

n=100
def sieve_of_eratosthenes(n: int):
    sieve = [True] * (n+1)

    sieve[0] = sieve[1] = False

    for i in range(2, (n+1)//2):
        if sieve[i]:
            for j in range(i*2, n+1, i):
                sieve[j] = False

    for i in range(n+1):
        if sieve[i]:
            print(i, end=" ")
    print()

if __name__ == "__main__":
    sieve_of_eratosthenes(100)


