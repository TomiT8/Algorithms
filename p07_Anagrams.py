# todo:
#   Napíšte funkciu, ktorá nájde všetky anagramy daného slova z poskytnutého zoznamu. Nájdené slová by sa mali vrátiť ako zoznam.

# todo:
#   Vysvetlenie: Čo je to anagram? Sú to dve slová, ktoré pozostávajú z rovnakých písmen. Napríklad:
#   'listen' & 'silent' == true
#   'cat' & 'tap' == false
#   'meta' & 'mata' == false
#   'night' & 'thing' == true

# todo:
#   Algorytmus by mal fungovať takto:
#   anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
#   anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
#   anagrams('laser', ['lazing', 'lazy', 'lacer']) => []

from typing import List


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    sorted_word = sorted(word)
    anagrams_list = []

    for w in lst_of_words:
        if sorted(w) == sorted_word:
            anagrams_list.append(w)

    return anagrams_list

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) #=> ['aabb', 'bbaa']
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) #=> ['carer', 'racer']
print(anagrams('laser', ['lazing', 'lazy', 'lacer'])) #=> []