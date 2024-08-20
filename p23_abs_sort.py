"""
Zadanie: Chceme neusporiadaný zoznam čísel usporiadať podľa absolutnej hodnoty.
[2,-5,3,-2,2,1,-1,-9,-7,8] -> [-1,1,-2,2,2,3,-5,-7,8,-9]
"""

from typing import List


def abs_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = abs(arr[0])

    left_half = [x for x in arr if abs(x) < pivot]
    middle = [x for x in arr if abs(x) == pivot and x<0] + [x for x in arr if abs(x) == pivot and x>0]
    right_half = [x for x in arr if abs(x) > pivot]

    return abs_sort(left_half) + middle + abs_sort(right_half)


if __name__ == "__main__":
    unsorted_list = [2, -5, 3, -2, 2, 1, -1, -9, -7, 8]  #-> [-1,1,-2,2,2,3,-5,-7,8,-9]
    print(abs_sort(unsorted_list))
