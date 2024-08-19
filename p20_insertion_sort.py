from typing import List

def insert_sort(unsorted: List[int]) -> List[int]:
    sorted_list = []
    for i in range(len(unsorted)):
        j = 0
        while j < len(sorted_list) and sorted_list[j] < unsorted[i]:
            j += 1
        sorted_list.insert(j, unsorted[i])
    return sorted_list


if __name__ == "__main__":
    unsorted = [8, 4, 2, 5, 3, 1, 7, 2, 9]
    print(insert_sort(unsorted))
