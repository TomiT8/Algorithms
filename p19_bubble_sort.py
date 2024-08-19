from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    for i in range(len(numbers) - 1):
        print(numbers)
        snapped = False
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                snapped = True
        if not snapped:
            return numbers
    return numbers


if __name__ == "__main__":
    numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9]
    print(bubble_sort(numbers))
