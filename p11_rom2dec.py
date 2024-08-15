"""Převod římských číslic na arabské
Napište funkci, která převede římské číslo na arabské (běžné celé číslo).
Římské číslice jsou I, V, X, L, C, D, M a mají hodnoty 1, 5, 10, 50, 100, 500, 1000.

Tip:
Při převodu je třeba mít na paměti, že pokud menší číslice předchází větší,
hodnota menší číslice se odečítá (např. IV = 4, IX = 9).

rom2dec('MMXXIV') -> 2024
"""

rom_num = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


# počítať od konca

def rom2dec(romstr: str):
    result = 0
    prev_value = 0

    for char in reversed(romstr):
        current_value = rom_num[char]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value
    return result


if __name__ == "__main__":
    rom2dexs = ['MMXXIV']
    for rom in rom2dexs:
        print(f"'{rom} -> {rom2dec(rom)}'")
