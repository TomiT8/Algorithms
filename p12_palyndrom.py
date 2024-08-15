"""Palindrom
Napište funkci, který zjistí, zda je daný řetězec palindrom.
Palindrom je řetězec, který se čte stejně zleva i zprava,
například 'madam' nebo 'racecar'.

is_palindrom("madam") -> True
is_palindrom("kobylamamalybok") -> True
is_palindrom("kokos") -> False
"""


def is_palyndrom(text: str) -> str:
    text = text.lower()
    return text == text[::-1]


if __name__ == "__main__":
    prem = ["Madam", "kobylamamalybok", "kokos"]
    for p in prem:
        print(f'"{p}" -> "{is_palyndrom(p)}"')
