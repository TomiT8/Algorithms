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


def binary_search_iter(n: int, numbers: list[int]) -> int:
    start = 0
    end = len(numbers)-1

    while start < end -1:
        mid = (start + end) // 2

        if numbers[mid] == n:
            return mid
        if numbers[mid] > n:
            end = mid
        else:
            start = mid
    return -1


def binary_search_rec(n: int, numbers: list[int], start: int = 0, end: int = None) -> int:
    if end is None:
        end = len(numbers) - 1

    if start >= end -1:
        return -1

    mid = (start + end) // 2

    if numbers[mid] == n:
        return mid
    if numbers [mid] > n:
        #end = mid
        return binary_search_rec(n, numbers, start=start, end=mid)

        # start = mid
    return binary_search_rec(n, numbers, start=mid, end=end)


if __name__ == "__main__":
    print(search(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print(search(7, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print("binary:")
    print(binary_search_iter(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print(binary_search_iter(7, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print("recurse")
    print(binary_search_rec(5, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))
    print(binary_search_rec(7, [1, 1, 1, 2, 2, 3, 5, 6, 8, 9, 10, 12, 15, 20]))