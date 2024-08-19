""" Sort MINIMAX
Vyhľadám v nezotriedenej postupnosti najmenší/najväčší prvek
a vložím ho na koniec zoradenej postúpnosti
unsorted = [8, 4, 2, 5, 3, 1, 7, 2, 9]
"""
# unsorted = [8, 4, 2, 5, 3, 1, 7, 2, 9]
#
# sorted_list = sorted(unsorted)
# print(sorted_list)


# kým pôvodný zoznam nie je prázdny
# nájdem namenší prvok v pôvodnom zozname
# nájdený prvok vložím na koniec nového zoznamu
# nájdený prvok odstránim z pôvodného zoznamu


# unsorted = [8, 4, 2, 5, 3, 1, 7, 2, 9]
# sorted_list = []
#
# while len(unsorted) > 0:
#     minimal_value = unsorted[0]
#     minimal_index = 0
#
#     for i in range(1, len(unsorted)):
#         if unsorted[i] < minimal_value:
#             minimal_value = unsorted[i]
#             minimal_index = i
#     print(f"Minimal value: {minimal_value} at index {minimal_index}")
#
#     sorted_list.append(minimal_value)
#     unsorted.pop(minimal_index)
#     print(f"Unsorted list: {unsorted}")
#     print(f"Sorted list: {sorted_list}")
#     print("-"*80)

"""funkcia"""

# from typing import List
#
# sorted_list = []
#
#
# def minimax(unsorted: List[int]) -> List[int]:
#     while len(unsorted) > 0:
#         minimal_value = unsorted[0]
#         minimal_index = 0
#
#         for i in range(1, len(unsorted)):
#             if unsorted[i] < minimal_value:
#                 minimal_value = unsorted[i]
#                 minimal_index = i
#         # print(f"Minimal value: {minimal_value} at index {minimal_index}")
#
#         sorted_list.append(minimal_value)
#         unsorted.pop(minimal_index)
#         # print(f"Unsorted list: {unsorted}")
#         # print(f"Sorted list: {sorted_list}")
#         # print("-"*80)
#     return sorted_list
#
#
# if __name__ == "__main__":
#     unsorted = [8, 4, 2, 5, 3, 1, 7, 2, 9]
#     print(minimax(unsorted))


""" selection sort """

from typing import List


def minimax(unsorted: List[int]) -> List[int]:
    """
    Computational complexity:
    - time: O(n^2)
    - memory: O(n)
    :param unsorted:
    :return: sorted
    """
    number_of_iterations = 0
    sorted_list = []
    #print(f"Unsorted list: {unsorted}")
    # dokud původní seznam není prázdný
    while len(unsorted) > 0:
        # najdeme nejmenší prvek v původním seznamu
        minimal_value = unsorted[0]
        minimal_index = 0
        # projdeme celý seznam
        for i in range(1, len(unsorted)):
            number_of_iterations += 1
            # pokud najdeme číslo menší, než jaké je uložené v minimal_value
            if unsorted[i] < minimal_value:
                # do minimal_value uložíme tuto hodnotu
                minimal_value = unsorted[i]
                # do minimal_index vložím index této hodonoty
                minimal_index = i
        #print(f"Minimal value: {minimal_value} at index {minimal_index}.")
        # nalezený prvek vložím na konec nového seznamu
        sorted_list.append(minimal_value)
        # nalezený prvek odstraním z původního seznamu
        unsorted.pop(minimal_index)
        #print(f"Unsorted list: {unsorted}")
        #print(f"Sorted list:   {sorted_list}")
        #print('-'*80)
    print(f"Number of iterations: {number_of_iterations}")
    return sorted_list


if __name__ == '__main__':
    unsorted_list = [8, 4, 2, 5, 3, 1, 7, 2, 9, 14, 4, 2]
    print(minimax(unsorted_list))