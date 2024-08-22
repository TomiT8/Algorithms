"""Vyhodnocení výrazu v postfixové notaci (Reverse Polish Notation - RPN)

Zadání:
Napište funkci, která vyhodnotí aritmetický výraz zadaný v postfixové notaci.

Například:
"1 2 +" -> 3
"8 2 /" -> 4

"5 1 2 + 4 * + 3 -" ->
"5 3 4 * + 3 -" ->
"5 12 + 3 -" ->
"17 3 -" ->
"14" -> 14.
"
"""

def rpn(nstring: str) -> int:
    stack = []

    for t in nstring.split():
        if t.isdigit():
            stack.append(int(t))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
        if t == "+":
            stack.append(num1 + num2)
        if t == "-":
            stack.append(num1 - num2)
        if t == "*":
            stack.append(num1 * num2)
        if t == "/":
            stack.append(num1 / num2)
    return stack.pop()


if __name__ == '__main__':
    strings = ["1 2 +", "8 2 /", "5 1 2 + 4 * + 3 -"]
    for s in strings:
        print(f"'{s}' -> {rpn(s)}")
