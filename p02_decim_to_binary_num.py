# d = int(input("Zadaj číslo väčšie alebo rovné 0: "))

# binary_string = ""
#
# while d > 0:
#     r = d % 2
#
#     if r == 1:
#         binary_string = "1" + binary_string
#     else:
#         binary_string = "0" + binary_string
#
#     d = d // 2
#
#     if d == 0:
#         print(binary_string)

def dec2bin(d):
    binary_string = ""

    while True:
        r = d % 2

        if r == 1:
            binary_string = "1" + binary_string
        else:
            binary_string = "0" + binary_string

        d = d // 2

        if d == 0:
            return binary_string


# print(dec2bin(d))

for i in range(1, 21):
    print(f"{i}: {dec2bin(i)}")
