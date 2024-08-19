# pre každý prvok v zozname
# Nájdem najmenší prvok v nezatriedenej časti zoznamu
# Nájdený prvok prehodím s prvýmprvkom nezoradeného zoznamu

# numbers = [8, 4, 2, 5, 3, 1, 7, 2, 9]
#
# for i in range(len(numbers)):
#     minimal_value = numbers[i]
#     minimal_index = i
#     for j in range(i+1, len(numbers)):
#        if numbers[j] < minimal_value:
#            minimal_value = numbers[j]
#            minimal_index = j
#     numbers[i], numbers[minimal_index] = numbers[minimal_index], numbers[i]
#
# print(numbers)


"""funkcia"""

from typing import List


def seletion_numbers(numbers: List[int]) -> List[int]:
    for i in range(len(numbers)):
        minimal_value = numbers[i]
        minimal_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < minimal_value:
                minimal_value = numbers[j]
                minimal_index = j
        numbers[i], numbers[minimal_index] = numbers[minimal_index], numbers[i]
    return numbers


if __name__ == "__main__":
    numbers = [8, 4, 2, 5, 3, 14, 7, 2, 28]
    print(seletion_numbers(numbers))
