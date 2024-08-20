"""
Zadanie: Usporiadame zoznam celých čísel tak, že najprv budú všetky nepárne čísla (usporiadané podľa veľkosti)
a následke všetky párne čísla (urporiadané podľa veľkosti).
[5, 3, 4, 2, -6, 7, -7, 8, 1, 2] -> [-7, 1, 3, 5, 7, -6, 2, 2, 4]
"""

from typing import List
from p22_quick_sort import quick_sort


def add_even_quicksort(arr: List[int]) -> List[int]:
    return quick_sort([x for x in arr if x %2]) + quick_sort([x for x in arr if x %2 == 0])


if __name__ == "__main__":
    unsorted_list = [5, 3, 4, 2, -6, 7, -7, 8, 1, 2]  #-> [-7,1,3,5,7,-6,2,2,4]
    print(add_even_quicksort(unsorted_list))
