"""
Zátvorky
Napíšte funkciu, ktorá ma ako parameter string obsahujúce zátvorky.
Funkcia vráti True, ak sú zátvorky "správne", inak False.

Musí byť zabezpečený správny počet pravých a správny počet pravých zátvoriek.

()          -> Ture
(())        -> True
)(          -> False
(()         -> False
(()))(      -> False
(()))((())  -> False
"""


def brackets(s):
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return not stack

if __name__ == "__main__":
    words = ["()", "(())", ")(", "(()", "(()))(", "(()))((())"]
    for w in words:
        print(f"{w} -> {brackets(w)}")
    print()
    print()


def brackets2(s):
    stack = []

    for char in s:
        if char in "([{<":
            stack.append(char)
        elif char == ")":
            if not stack or stack.pop() != "(":
                return False
        elif char == "]":
            if not stack or stack.pop() != "[":
                return False
        elif char == "}":
            if not stack or stack.pop() != "{":
                return False
        elif not stack or char == "<":
            if stack.pop() != ">":
                return False
    return not stack


if __name__ == "__main__":
    words = ["([)]", "([])", "([][{}])", "({[]<[]>}())", "({[][<]>}())"]
    for w in words:
        print(f"{w} -> {brackets2(w)}")
