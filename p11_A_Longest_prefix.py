"""Vyhledání nejdelšího společného prefixu
Napište funkci, která najde nejdelší společný prefix (počáteční část) všech řetězců v seznamu.
Pokud žádný společný prefix neexistuje, funkce by měla vrátit prázdný řetězec.

longest_prefix(['abba', 'abeceda', 'ababa']) -> 'ab'
longest_prefix(['abba', 'abeceda', 'tata']) -> ''
"""

def longest_prefix(strs: list) -> str:
    if not strs:
        return ""
    pref = strs[0]
    for n in strs[1:]:
        while not n.startswith(pref):
            pref = pref[:-1]
            if not pref:
                return ""
    return pref


if __name__ == "__main__":
    longest_prefixs = (['abba', 'abeceda', 'ababa'],['abba', 'abeceda', 'tata'])
    for pref in longest_prefixs:
        print(f"{pref} -> '{longest_prefix(pref)}'")