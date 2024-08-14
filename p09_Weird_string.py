# todo:
#   Napíšte funkciu WeIrD CaSe, ktorá prijme reťazec a vráti ho so všetkými párnymi číslami ako znaky, všetky veľké a nepárne písmená ako malé. Použite indexovanie od nuly.

# todo:
#   Algoritmus by mal fungovať nasledovne:
#   to_weird_case('String') ## => return 'StRiNg'
#   to_weird_case('Algorithms and data structures') ## => return 'AlGoRiThMs AnD DaTa StRuCt###


def to_weird_case(string: str) -> str:
    new_word = string.split()
    result = ""

    for word in new_word:
        for i in range(len(word)):
            if i % 2 == 0:
                result += word[i].upper()
            else:
                result += word[i].lower()
        result += " "
    return result.strip()


if __name__ == "__main__":
    strings = ['String', 'Algorithms and data structures']
    for one_string in strings:
        print(f"{one_string} -> '{to_weird_case(one_string)}'")
