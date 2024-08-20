"""
zadanie: Usporaidať texty v zozname podľa ich dĺžky:
["Ahoj", "Hello", "Hi", "Nazdar", "Čau"] -> ["Hi", "Čau", "Ahoj", "Hello", "Nazdar"]
"""

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
