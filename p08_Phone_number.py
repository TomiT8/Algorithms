# todo:
#   Napíšte funkciu, ktorá vezme zoznam 11 celých čísel a vráti reťazec vo formáte telefónneho čísla.

# todo:
#   Algoritmus by mal fungovať nasledovne:
#   create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
#   => returns "(+12) 345-678-901"###

from typing import List


def create_phone_number(n: List[int]) -> str:
    return f'(+{n[0]}{n[1]}) {n[2]}{n[3]}{n[4]}-{n[5]}{n[-5]}{n[-4]}-{n[-3]}{n[-2]}{n[-1]}'


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))
