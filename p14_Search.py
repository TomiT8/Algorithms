"""
Napíš funkciu, ktorá má ako vstupný parameter usporiadaný zoznam.
Funkcia má pre danú hodnotu vypísať index, na ktorej sa v zozname nachádza.
search(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20] -> 6
search(7, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20] -> -1
"""


def search(n: int, numbers: list[int]) -> int:
    for i in range(len(numbers)):
        if numbers[i] == n:
            return i
        if numbers[i] > n:
            return -1
    return -1


if __name__ == "__main__":
    print(search(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print(search(7, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
