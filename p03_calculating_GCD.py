# a = int(input("Zadaj číslo a: "))
# b = int(input("Zadaj číslo b: "))
#
# while True:
#     if a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     else:
#         print(f"Največšís poločný deliteľ je {a} a {b} je {a}.")
#         break


# a = int(input("Zadaj číslo a: "))
# b = int(input("Zadaj číslo b: "))
#
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
#
# print(f"Največšís poločný deliteľ je {a} a {b} je {a}.")


a = int(input("Zadaj číslo a: "))
b = int(input("Zadaj číslo b: "))

def calcgd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(f"Največšís poločný deliteľ je {a} a {b} je {calcgd(a,b)}.")
