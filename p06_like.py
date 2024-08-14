# todo:
#   Cvičenie 1: Páči sa mi to!
#   Implementujte systém zobrazovania počtu „lajkov“ známy z Facebooku.
#   Vysvetlenie: Funkcia „páči sa mi“ by mala zadávať zoznam mien ako vstup ľudí, ktorým sa „páči“ daný príspevok / fotografiu, a vydávať správne naformátovaný text.

# todo
#   Nakoniec by mal algoritmus fungovať takto:
#   likes([])  ## => "nobody likes it"
#   likes(["Peter"])  ## => "Peter likes it!"
#   likes(["Peter", "Anna"])  ## => "Peter and Anna like it"
#   likes(["Peter", "Anna", "Mark"])  ## => "Peter, Anna and Mark like it"
#   likes(["Peter", "Anna", "Mark", "Ola"])  ## => "Peter, Anna and 2 other people like it"


from typing import List


def likes(names: List[str]) -> str:
    if len(names) == 0:
        return "nobody likes it"
    if len(names) == 1:
        return f"{names[0]} likes it!"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} likes it!"
    if len(names) == 3:
        return f"{names[0]} and {names[1]} and {names[2]} likes it!"
    return f"{names[0]} and {names[1]} and {len(names)} other people like it!"


if __name__ == '__main__':
    list_of_likes = [[], ["Peter"], ["Peter", "Anna"], ["Peter", "Anna", "Mark"], ["Peter", "Anna", "Mark", "Ola"],
                     ["Peter", "Anna", "Mark", "Ola", "Klára"]]

    for name in list_of_likes:
        print(f'{name}: {likes(name)}')
