from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left_half = []
    right_half = []
    middle = []

    for x in arr:
        if x < pivot:
            left_half.append(x)
        elif x > pivot:
            right_half.append(x)
        else:
            middle.append(x)

    return quick_sort(left_half) + middle + quick_sort(right_half)


if __name__ == "__main__":
    unsorted_list = [8, 4, 2, 5, 3, 1, 7, 2, 9]
    print(quick_sort(unsorted_list))
