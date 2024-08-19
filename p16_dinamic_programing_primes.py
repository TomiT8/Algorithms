"""
Výpis všetkých prvočísel do zadaného n (10000) s využitím dinamického programovania
"""

# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         print(f"Testujem deliteľnosť: {i}")
#         if n % i == 0:
#             return False
#     return True
#
#
# vypísať všetky prvočísla menšie než n (10000)
# def print_n_prime_numbers(n: int):
#     for i in range(n+1):
#         if is_prime(i):
#             print(i, end=" ")
#     print()
#
#
# if __name__ == "__main__":
#     print_n_prime_numbers(100)

"""dinamické programovanie"""


from typing import List


def is_prime(n: int, memory: List[int]) -> bool:
    if n < 2:
        return False
    for i in memory:
        if i > (n**0.5)+1:
            return True
        #print(f"Testuji dělitelnost {i}")
        if n % i == 0:
            return False
    return True


# vypsat všechna prvočísla menší než n (10000)
def print_n_prime_numbers(n: int):
    memory = []
    for i in range(n+1):
        if is_prime(i, memory):
            memory.append(i)
    print(memory)


if __name__ == '__main__':
    print_n_prime_numbers(100000)
    #print(is_prime(997))