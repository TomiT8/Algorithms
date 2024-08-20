from typing import List


def merge_sort(unsorted_list: List[int]) -> List[int]:
    if len(unsorted_list) <= 1:
        return unsorted_list

    mid = len(unsorted_list) // 2
    left_half = merge_sort(unsorted_list[:mid])
    right_half = merge_sort(unsorted_list[mid:])

    # print(f"{left_half}, {right_half}")

    sorted_list = []
    left_index, right_index = 0, 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1

    sorted_list.extend(left_half[left_index:])
    sorted_list.extend(right_half[right_index:])

    return sorted_list


if __name__ == "__main__":
    unsorted_list = [8, 4, 2, 5, 3, 1, 7, 2, 9]
    print(merge_sort(unsorted_list))
