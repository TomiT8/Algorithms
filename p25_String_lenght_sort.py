"""
zadanie: Usporaidať texty v zozname podľa ich dĺžky:
["Ahoj", "Hello", "Hi", "Nazdar", "Čau"] -> ["Hi", "Čau", "Ahoj", "Hello", "Nazdar"]
"""

"""quick sort"""
def string_lenght_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = len(arr[0])

    left_half = [x for x in arr if len(x) < pivot]
    middle = [x for x in arr if len(x) == pivot]
    right_half = [x for x in arr if len(x) > pivot]

    return string_lenght_sort(left_half) + middle + string_lenght_sort(right_half)


if __name__ == "__main__":
    unsorted_list = ["Ahoj", "Hello", "Hi", "Nazdar", "Čau"]
    print(string_lenght_sort(unsorted_list))


""" merge sort"""


def string_lenght_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = string_lenght_sort(arr[:mid])
    right_half = string_lenght_sort(arr[mid:])

    # print(f"{left_half}, {right_half}")

    sorted_list = []
    left_index, right_index = 0, 0

    while left_index < len(left_half) and right_index < len(right_half):
        if len(left_half[left_index]) < len(right_half[right_index]):
            sorted_list.append(left_half[left_index])
            left_index += 1
        else:
            sorted_list.append(right_half[right_index])
            right_index += 1

    sorted_list.extend(left_half[left_index:])
    sorted_list.extend(right_half[right_index:])

    return sorted_list


if __name__ == "__main__":
    unsorted_list = ["Ahoj", "Hello", "Hi", "Nazdar", "Čau"]
    print(string_lenght_sort(unsorted_list))