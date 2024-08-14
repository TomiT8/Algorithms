"""
factors(5) -> [5]
factors() -> []

"""

n = int(input("Zadaj číslo n rovné alebo väčšie ako 2: "))

def prv(n):
    p = []
    delitel = 2
    while n > 1:
        if n % delitel == 0:
            p.append(delitel)
            n //= delitel
        else:
            delitel += 1
    return p


print(prv(n))
